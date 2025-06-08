from django.urls import path

from . import views 

urlpatterns = [

    path('courses-list/', views.CoursesListView.as_view(), name='courses_list'),

    path('courses-detail/<str:uuid>', views.CourseDetailView.as_view(),name='course-detail'),

    path('home/',views.HomeView.as_view(), name='home'),

    path('instructor/', views.InstructorCoursesView.as_view(), name='instructor_courses'),

    path('create-course/', views.CourseCreateView.as_view(), name='course_create'),

    path('instructor-course-detail/<str:uuid>', views.InstructorCoursesDetailView.as_view(),name='instructor-course-detail'),

    path('instructor-course-delete/<str:uuid>', views.InstructorCoursesDeleteView.as_view(),name='instructor-course-delete'),

    path('instructor-course-update/<str:uuid>', views.InstructorCoursesUpdateView.as_view(),name='instructor-course-update'),

]