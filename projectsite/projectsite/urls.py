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
from record.views import HomePageView, ProfessorListView, CourseListView, StudentListView, EnrollmentListView, AssignmentListView, GradeListView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('professors/', ProfessorListView.as_view(), name='professor-list'),
    path('courses/', CourseListView.as_view(), name='course-list'),
    path('students/', StudentListView.as_view(), name='student-list'),
    path('enrollments/', EnrollmentListView.as_view(), name='enrollment-list'),
    path('assignments/', AssignmentListView.as_view(), name='assignment-list'),
    path('grades/', GradeListView.as_view(), name='grade-list'),
]

