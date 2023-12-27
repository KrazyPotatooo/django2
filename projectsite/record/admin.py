from django.contrib import admin
from .models import Professor, Course, Student, Enrollment, Assignment, Grade
# Register your models here.

@admin.register(Professor)
class ProfessorAdmin(admin. ModelAdmin):
    list_display = ("FirstName", "LastName", "Email", "Department","created_at","updated_at")
    search_fields = ("FirstName", "LastName", "Email", "Department")

@admin.register(Course)
class CourseAdmin(admin. ModelAdmin):
    list_display = ("CourseName", "Department", "ProfessorID","created_at","updated_at")
    search_fields = ("CourseName", "Department", "ProfessorID__FirstName", "ProfessorID__LastName", "ProfessorID__Email")

@admin.register(Student)
class StudentAdmin(admin. ModelAdmin):
    list_display = ("FirstName", "LastName", "Email","created_at","updated_at")
    search_fields = ("FirstName", "LastName", "Email")

@admin.register(Enrollment)
class EnrollmentAdmin(admin. ModelAdmin):
    list_display = ("StudentID", "CourseID","created_at","updated_at")
    search_fields = ("StudentID__FirstName", "StudentID__LastName", "CourseID__CourseName")

@admin.register(Assignment)
class AssignmentAdmin(admin. ModelAdmin):
    list_display = ("AssignmentName", "Deadline", "CourseID","created_at","updated_at")
    search_fields = ("AssignmentName", "CourseID__CourseName")

@admin.register(Grade)
class GradeAdmin(admin. ModelAdmin):
    list_display = ("StudentID", "AssignmentID", "Score","created_at","updated_at")
    search_fields = ("StudentID__FirstName", "StudentID__LastName", "AssignmentID__AssignmentName")