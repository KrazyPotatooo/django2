from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Professor(BaseModel):
    ProfessorID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    Email = models.EmailField()
    Department = models.CharField(max_length=255)
    ProfileImage = models.ImageField(upload_to='professor_images/',blank=True, null=True)

    def __str__(self):
        return f"{self.ProfileImage} {self.FirstName} {self.LastName}"

class Course(BaseModel):
    CourseID = models.AutoField(primary_key=True)
    CourseName = models.CharField(max_length=255)
    Department = models.CharField(max_length=255)
    ProfessorID = models.ForeignKey(Professor, on_delete=models.CASCADE)

    def __str__(self):
        return self.CourseName

class Student(BaseModel):
    StudentID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    Email = models.EmailField()
  
    def __str__(self):
        return f"{self.FirstName} {self.LastName}"

class Enrollment(BaseModel):
    StudentID = models.ForeignKey(Student, on_delete=models.CASCADE)
    CourseID = models.ForeignKey(Course, on_delete=models.CASCADE)

class Assignment(BaseModel):
    AssignmentID = models.AutoField(primary_key=True)
    AssignmentName = models.CharField(max_length=255)
    Deadline = models.DateField()
    CourseID = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.AssignmentName

class Grade(BaseModel):
    GradeID = models.AutoField(primary_key=True)
    StudentID = models.ForeignKey(Student, on_delete=models.CASCADE)
    AssignmentID = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    Score = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Grade for {self.StudentID} - {self.AssignmentID}: {self.Score}"
