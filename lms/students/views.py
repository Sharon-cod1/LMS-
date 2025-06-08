from django.shortcuts import render,redirect
from .forms import ProfileForm, StudentForm
from django.views import View

from django.contrib.auth.hashers import make_password

from django.db import transaction

from lms.utility import send_email

import threading

# Create your views here.

class StudentRegisterView(View):

    def get(self,request,*args,**kwargs):

        profile_form = ProfileForm()

        student_form = StudentForm()

        data ={
            'profile_form' : profile_form,
            'student_form' : student_form
        }

        return render(request,'students/students-register.html',context=data)
    
    def post(self, request, *args , **kwrgs):

        profile_form = ProfileForm(request.POST)

        student_form = StudentForm(request.POST, request.FILES)

        print(profile_form.errors)

        print(student_form.errors)


        if profile_form.is_valid():

            with transaction.atomic():


                profile = profile_form.save(commit=False)

                email = profile_form.cleaned_data.get('email')

                password = profile_form.cleaned_data.get('password')

                profile.username = email

                profile.role = 'Student'

                profile.password = make_password(password)

                profile.save()


                if student_form.is_valid():

                    student = student_form.save(commit= False)

                    student.profile = profile

                    student.name = f' {profile.first_name} {profile.last_name}'

                    student.save()
                    
                    # Send email notification
                    subject = 'Successfully registered'

                    recipient = student.profile.email

                    template = 'email/success-registration.html'

                    context = {
                        'name': student.name,
                        'email': student.profile.email,
                        'password': password
                    }

                    thread = threading.Thread(target=send_email,args=(subject,recipient,template,context))

                    thread.start()

                    # send_email(subject, recipient, template, context)


                    return redirect('login')
            
        data = {
                'profile_form' : profile_form,
                'student_form' : student_form
            }
            
        return render(request, 'students/students-register.html', context=data)