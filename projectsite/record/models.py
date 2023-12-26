from django.db import models

# Create your models here.

class Professor(models.Model):
    ProfessorID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    Email = models.EmailField()
    Department = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.FirstName} {self.LastName}"

class Course(models.Model):
    CourseID = models.AutoField(primary_key=True)
    CourseName = models.CharField(max_length=255)
    Department = models.CharField(max_length=255)
    ProfessorID = models.ForeignKey(Professor, on_delete=models.CASCADE)

    def __str__(self):
        return self.CourseName

class Student(models.Model):
    StudentID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    Email = models.EmailField()

    def __str__(self):
        return f"{self.FirstName} {self.LastName}"

class Enrollment(models.Model):
    StudentID = models.ForeignKey(Student, on_delete=models.CASCADE)
    CourseID = models.ForeignKey(Course, on_delete=models.CASCADE)

class Assignment(models.Model):
    AssignmentID = models.AutoField(primary_key=True)
    AssignmentName = models.CharField(max_length=255)
    Deadline = models.DateField()
    CourseID = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.AssignmentName

class Grade(models.Model):
    GradeID = models.AutoField(primary_key=True)
    StudentID = models.ForeignKey(Student, on_delete=models.CASCADE)
    AssignmentID = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    Score = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Grade for {self.StudentID} - {self.AssignmentID}: {self.Score}"
