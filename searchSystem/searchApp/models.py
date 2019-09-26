from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class School(models.Model):
    name =  models.CharField(max_length = 100)
    
    def __str__(self):
        return self.name

class Faculty(models.Model):
    name = models.CharField(max_length = 40)

    def __str__(self):
        return self.name

class Department(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete = models.CASCADE)
    name = models.CharField(max_length = 500)

    def __str__(self):
        return self.name

class Grade(models.Model):
    type = models.CharField(max_length = 100)

    def __str__(self):
        return self.type

class Certificate_Type(models.Model):
    name = models.CharField(max_length = 20)

    def __str__(self):
        return self.name

class Student(models.Model):
    school = models.ForeignKey(School, on_delete = models.CASCADE)
    department = models.ForeignKey(Department, on_delete = models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete = models.CASCADE)
    certificate = models.ForeignKey(Certificate_Type, on_delete = models.CASCADE)
    fullname = models.CharField(max_length = 100)
    year_of_grad = models.IntegerField(default = "")

    def __str__(self):
        return self.fullname

