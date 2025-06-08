from django import template

from students.models import Students

from instructors.models import Instructors



register = template.Library()

@register.simple_tag
def convert_uppercase(text):

    return text.upper()

@register.simple_tag
def user_role_checking(request , roles):

    role = roles.split(',')

    if request.user.is_authenticated and request.user.role in roles :

        return True
    
    return False


@register.simple_tag
def get_image(request):

    if request.user.is_authenticated:

        if request.user.role == 'Student':

            student = Students.objects.get(profile=request.user)

            return student.image
        
        elif request.user.role == 'Instructor':

            instructor = Instructors.objects.get(profile=request.user)

            return instructor.image