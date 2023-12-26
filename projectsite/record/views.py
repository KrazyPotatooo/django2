from django.shortcuts import render

# Create your views here.
# myapp/views.py
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Professor, Course, Student, Enrollment, Assignment, Grade
from .forms import ProfessorForm,CourseForm,StudentForm,AssignmentForm,GradeForm,EnrollmentForm
from django.urls import reverse_lazy

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
    paginate_by = 5

    def get_queryset(self):
        return Professor.objects.all()
    
class ProfessorCreateView(CreateView):
    model = Professor
    form_class = ProfessorForm
    template_name = 'professor_add.html'
    success_url = reverse_lazy('professor-list')
    
class ProfessorUpdateView(UpdateView):
    model = Professor
    form_class = ProfessorForm
    template_name = 'professor_edit.html'
    success_url = reverse_lazy('professor-list')
    
class ProfessorDeleteView(DeleteView):
    model = Professor
    template_name = 'professor_del.html'
    success_url = reverse_lazy('professor-list')  

class CourseListView(ListView):
    model = Course
    template_name = 'course_list.html'
    context_object_name = 'courses'
    paginate_by = 5

    def get_queryset(self):
        return Course.objects.all()
    
class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'course_add.html'
    success_url = reverse_lazy('course-list')
    
class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'course_edit.html'
    success_url = reverse_lazy('course-list')
    
class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'course_del.html'
    success_url = reverse_lazy('course-list')  

class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'
    context_object_name = 'students'
    paginate_by = 5

    def get_queryset(self):
        return Student.objects.all()

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_add.html'
    success_url = reverse_lazy('student-list')
    
class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_edit.html'
    success_url = reverse_lazy('student-list')
    
class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_del.html'
    success_url = reverse_lazy('student-list')  
    
class EnrollmentListView(ListView):
    model = Enrollment
    template_name = 'enrollment_list.html'
    context_object_name = 'enrollments'
    paginate_by = 5

    def get_queryset(self):
        return Enrollment.objects.all()
    
class EnrollmentCreateView(CreateView):
    model = Enrollment
    form_class = EnrollmentForm
    template_name = 'enrollment_add.html'
    success_url = reverse_lazy('enrollment-list')
    
class EnrollmentUpdateView(UpdateView):
    model = Enrollment
    form_class = EnrollmentForm
    template_name = 'enrollment_edit.html'
    success_url = reverse_lazy('enrollment-list')
    
class EnrollmentDeleteView(DeleteView):
    model = Enrollment
    template_name = 'enrollment_del.html'
    success_url = reverse_lazy('enrollment-list') 

class AssignmentListView(ListView):
    model = Assignment
    template_name = 'assignment_list.html'
    context_object_name = 'assignments'
    paginate_by = 5

    def get_queryset(self):
        return Assignment.objects.all()
    
class AssignmentCreateView(CreateView):
    model = Assignment
    form_class = AssignmentForm
    template_name = 'assignment_add.html'
    success_url = reverse_lazy('assignment-list')
    
class AssignmentUpdateView(UpdateView):
    model = Assignment
    form_class = AssignmentForm
    template_name = 'assignment_add.html'
    success_url = reverse_lazy('assignment-list')
    
class AssignmentDeleteView(DeleteView):
    model = Assignment
    template_name = 'assignment_del.html'
    success_url = reverse_lazy('assignment-list') 

class GradeListView(ListView):
    model = Grade
    template_name = 'grade_list.html'
    context_object_name = 'grades'
    paginate_by = 5

    def get_queryset(self):
        return Grade.objects.all()
    
class GradeCreateView(CreateView):
    model = Grade
    form_class = GradeForm
    template_name = 'grade_add.html'
    success_url = reverse_lazy('grade-list')
    
class GradeUpdateView(UpdateView):
    model = Grade
    form_class = GradeForm
    template_name = 'grade_edit.html'
    success_url = reverse_lazy('grade-list')
    
class GradeDeleteView(DeleteView):
    model = Grade
    template_name = 'grade_del.html'
    success_url = reverse_lazy('grade-list') 
