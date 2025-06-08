from django.shortcuts import render ,redirect

from django.views import View

from .models import Course , Categorychoice , Levelchoice

from .forms import CourseCreateForm

from instructors.models import Instructors

from django.db.models import Q

from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator 

from authentication.permissions import permission_roles

from lms.utility import get_recommended_courses

# Create your views here.

class CoursesListView(View):

    def get(self, request,*args, **kwargs):

        query = request.GET.get('query')
        
        course = Course.objects.all()

        if query:

            # Filter the courses based on the search query
            course = Course.objects.filter(Q(title__icontains=query)| 
                                           Q(description__icontains=query)|
                                           Q(instructor_name_icontains=query)|
                                           Q(category__icontains=query)|
                                           Q(type__icontains=query)|
                                           Q(level__icontains=query)|
                                           Q(fee__icontains=query))

        # Fetch all the courses from the database


        data ={'courses': course, 'page':'course-page', 'query': query}

        return render(request, 'courses/courses-list.html',context=data)

class CourseDetailView(View):

    def get(self, request, *args, **kwargs):

        uuid = kwargs.get('uuid')

        course = Course.objects.get(uuid=uuid)

        recommended_courses = get_recommended_courses(course)

        data = {'course' : course,'recommended_courses':recommended_courses}

        print(recommended_courses)


        return render (request,'courses/courses-details.html' ,context=data)

        
class HomeView(View):

    def get(self, request):

        data ={'page':'home-page'}

        return render(request, 'courses/home.html',context=data)

# @login_required(login_url='login')  

# @method_decorator(login_required(login_url='login'), name='dispatch')    #--- to access the instructor page you have to login first

@method_decorator(permission_roles(roles=['Instructor']), name='dispatch')
class InstructorCoursesView(View):

    def get(self, request,*args, **kwargs):

        instructor = Instructors.objects.get(profile= request.user)
        
        courses = Course.objects.filter(instructor=instructor)

        query = request.GET.get('query')

        if query:

            # Filter the courses based on the search query
            courses= Course.objects.filter(Q(title__icontains=query)| 
                                           Q(description__icontains=query)|
                                           Q(instructor_name_icontains=query)|
                                           Q(category__icontains=query)|
                                           Q(type__icontains=query)|
                                           Q(level__icontains=query)|
                                           Q(fee__icontains=query))

        data ={'page':'instructor-page','courses': courses, 'query': query}

        return render(request, 'courses/instructor-courses-list.html',context=data)
    
    

# normal way    
# class CourseCreateView(View):

#     def get(self, request):

#         form = Course.objects.all()
#         data = {'form': form, }
#         return render(request, 'courses/courses-create.html',context=data)
    
#     def post(self, request):

#         from_data = request.POST
#         image = request.FILES.get('image')
#         title = from_data.get('title')
#         description = from_data.get('description')
#         category = from_data.get('category')
#         level = from_data.get('level')
#         fee = from_data.get('fee')
#         offer_fee = from_data.get('offer_fee')
#         instructor = 'Jhone Doe'

#         course = Course.objects.create(
#             title = title,
#             description = description,
#             category = category,
#             level = level,
#             fee = fee,
#             offer_fee = offer_fee,
#             instructor = instructor,
#             image = image
#         )
#         course.save()
#         # Redirect to the instructor courses page after creating the course


#         return redirect('instructor_courses')



# with django form
@method_decorator(login_required(login_url='login'), name='dispatch')
class CourseCreateView(View):

    def get(self, request):

        form = CourseCreateForm()
        data = {'form': form, }
        return render(request, 'courses/courses-create.html',context=data)
    
    def post(self, request):

        form = CourseCreateForm(request.POST, request.FILES)

        instructor = Instructors.objects.get(id = 1)
        
        if form.is_valid():

            course = form.save(commit=False)

            course.instructor = instructor

            course.save()

            return redirect('instructor_courses')
        

        data = {'form': form, }
        # If the form is not valid, render the form again with error messages

        print(form.errors)
        return render(request, 'courses/courses-create.html',context={'form': form})
#         # Redirect to the instructor courses page after creating the course
#         return redirect('instructor_courses')
#         return render(request, 'courses/courses-create.html',context={'form': form})\

@method_decorator(login_required(login_url='login'), name='dispatch')
class InstructorCoursesDetailView(View):

    def get(self, request, *args, **kwargs):

        uuid = kwargs.get('uuid')

        course = Course.objects.get(uuid=uuid)

        data = {'course' : course}

        return render (request,'courses/instructor-courses-detail.html' ,context={'course' : course})

@method_decorator(login_required(login_url='login'), name='dispatch')   
class InstructorCoursesDeleteView(View):

    def get(self, request,args ,*kwargs):

        uuid = kwargs.get('uuid')

        course = Course.objects.get(uuid=uuid)

        course.delete()

        return redirect('instructor_courses')
        
@method_decorator(login_required(login_url='login'), name='dispatch')
class InstructorCoursesUpdateView(View):

    def get(self, request, *args, **kwargs):

        uuid = kwargs.get('uuid')

        course = Course.objects.get(uuid=uuid)

        form = CourseCreateForm(instance=course)

        data = {'form' : form}

        return render(request,'courses/instructor-courses-update.html', context=data)
    
    def post(self, request, *args, **kwargs):

        uuid = kwargs.get('uuid')

        course = Course.objects.get(uuid=uuid)

        form = CourseCreateForm(request.POST, request.FILES, instance=course)

        if form.is_valid():

            form.save()

            return redirect('instructor_courses')
        
        data = {'form' : form}
        # If the form is not valid, render the form again with error messages

        return render(request,'courses/instructor-courses-update.html', context=data)