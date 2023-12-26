"""
URL configuration for projectsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from record.views import HomePageView, ProfessorListView, ProfessorCreateView,ProfessorDeleteView,ProfessorUpdateView, CourseListView,CourseCreateView,CourseDeleteView,CourseUpdateView, StudentListView,StudentCreateView,StudentDeleteView,StudentUpdateView, EnrollmentListView,EnrollmentCreateView,EnrollmentDeleteView,EnrollmentUpdateView, AssignmentListView,AssignmentCreateView,AssignmentDeleteView,AssignmentUpdateView, GradeListView,GradeCreateView,GradeDeleteView,GradeUpdateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('professors/', ProfessorListView.as_view(), name='professor-list'),
    path('professor_list/add', ProfessorCreateView.as_view(), name='professor-add'),
    path('professor_list/<pk>', ProfessorUpdateView.as_view(), name='professor-edit'),
    path('professor_list/<pk>/delete', ProfessorDeleteView.as_view(), name='professor-delete'),
    
    path('courses/', CourseListView.as_view(), name='course-list'),
    path('course_list/add', CourseCreateView.as_view(), name='course-add'),
    path('course_list/<pk>', CourseUpdateView.as_view(), name='course-edit'),
    path('course_list/<pk>/delete', CourseDeleteView.as_view(), name='course-delete'),
    
    path('students/', StudentListView.as_view(), name='student-list'),
    path('student_list/add', StudentCreateView.as_view(), name='student-add'),
    path('student_list/<pk>', StudentUpdateView.as_view(), name='student-edit'),
    path('student_list/<pk>/delete', StudentDeleteView.as_view(), name='student-delete'),
    
    path('enrollments/', EnrollmentListView.as_view(), name='enrollment-list'),
    path('enrollment_list/add', EnrollmentCreateView.as_view(), name='enrollment-add'),
    path('enrollment_list/<pk>', EnrollmentUpdateView.as_view(), name='enrollment-edit'),
    path('enrollment_list/<pk>/delete', EnrollmentDeleteView.as_view(), name='enrollment-delete'),
    
    path('assignments/', AssignmentListView.as_view(), name='assignment-list'),
    path('assignment_list/add', AssignmentCreateView.as_view(), name='assignment-add'),
    path('assignment_list/<pk>', AssignmentUpdateView.as_view(), name='assignment-edit'),
    path('assignment_list/<pk>/delete', AssignmentDeleteView.as_view(), name='assignment-delete'),
    
    path('grades/', GradeListView.as_view(), name='grade-list'),
    path('grade_list/add', GradeCreateView.as_view(), name='grade-add'),
    path('grade_list/<pk>', GradeUpdateView.as_view(), name='grade-edit'),
    path('grade_list/<pk>/delete', GradeDeleteView.as_view(), name='grade-delete'),
]

