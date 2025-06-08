from django.core.mail import EmailMultiAlternatives

from django.template.loader import render_to_string

from django.conf import settings


def send_email(subject,recipient,template,context):

    mail = EmailMultiAlternatives(subject=subject,
                                  from_email=settings.EMAIL_HOST_USER,
                                  to=[recipient])
    
    context = render_to_string(template, context)

    mail.attach_alternative(context, "text/html")

    mail.send()

# function to get recommended courses

import pandas as pd

from sklearn.metrics.pairwise import cosine_similarity

from sklearn.feature_extraction.text import TfidfVectorizer

from course.models import Course


def get_recommended_courses(course):

    data = pd.DataFrame(Course.objects.all().values('id','title', 'description','type','category','tags','level','instructor_name','instructor_area_of_expertise__area'))



    data['all_fields'] = data['description']+' '+data['type']+' '+data['category']+' '+data['tags']+' '+data['level']+' '+data['instructor_name']+' '+data['instructor_area_of_expertise__area']
    
    data.drop(columns=['description','type','category','tags','level','instructor_name','instructor_area_of_expertise__area'],inplace=True)


    tfidf_vectorizer = TfidfVectorizer(max_features=200, stop_words='english')

    vector = tfidf_vectorizer.fit_transform(data['all_fields']).toarray()

    title = course.title
    
    similiarity=cosine_similarity(vector)

    my_course_id=data[data['title']==title].index[0]

    distance=sorted(list(enumerate(similiarity[my_course_id])),reverse=True,key=lambda vector:vector[1])

    recommended_courses_ids=[]

    for i in distance[0:10]:

        similarity_score = i[1]

        ids = data.iloc[i[0]].id

        if similarity_score > 0.1 and ids!=course.id:

            recommended_courses_ids.append(ids)

    recommended_courses = Course.objects.filter(id__in=recommended_courses_ids)

    return recommended_courses