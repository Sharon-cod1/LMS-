from django.urls import path
from . import views


urlpatterns = [

    path('instructor-register', views.InstructorRegisterView.as_view(), name='instructor-register'),
]