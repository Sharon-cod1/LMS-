from django.urls import path
from . import views


urlpatterns = [

    path('student-register', views.StudentRegisterView.as_view(), name='student-register'),
]