# myapp/forms.py
from django.forms import ModelForm
from django import forms
from .models import Professor, Course, Student, Enrollment, Assignment, Grade

class ProfessorForm(ModelForm):
    class Meta:
        model = Professor
        fields = "__all__"

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = "__all__"

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

class EnrollmentForm(ModelForm):
    class Meta:
        model = Enrollment
        fields = "__all__"

class AssignmentForm(ModelForm):
    Deadline = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Assignment
        fields = "__all__"

class GradeForm(ModelForm):
    class Meta:
        model = Grade
        fields = "__all__"
