from django.shortcuts import render

# Create your views here.
# myapp/views.py
from django.views.generic.list import ListView
from .models import Professor, Course, Student, Enrollment, Assignment, Grade

class HomePageView(ListView):
    model = Student
    context_object_name = 'home'
    template_name = "base.html"
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       return context
class ProfessorListView(ListView):
    model = Professor
    template_name = 'professor_list.html'
    context_object_name = 'professors'
    paginate_by = 10

    def get_queryset(self):
        return Professor.objects.all()

class CourseListView(ListView):
    model = Course
    template_name = 'course_list.html'
    context_object_name = 'courses'
    paginate_by = 10

    def get_queryset(self):
        return Course.objects.all()

class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'
    context_object_name = 'students'
    paginate_by = 10

    def get_queryset(self):
        return Student.objects.all()

class EnrollmentListView(ListView):
    model = Enrollment
    template_name = 'enrollment_list.html'
    context_object_name = 'enrollments'
    paginate_by = 10

    def get_queryset(self):
        return Enrollment.objects.all()

class AssignmentListView(ListView):
    model = Assignment
    template_name = 'assignment_list.html'
    context_object_name = 'assignments'
    paginate_by = 10

    def get_queryset(self):
        return Assignment.objects.all()

class GradeListView(ListView):
    model = Grade
    template_name = 'grade_list.html'
    context_object_name = 'grades'
    paginate_by = 10

    def get_queryset(self):
        return Grade.objects.all()
