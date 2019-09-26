from django.contrib import admin
from .models import School, Faculty, Department, Student, Grade, Certificate_Type

admin.site.register(School)
admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Certificate_Type)
admin.site.register(Grade)
admin.site.register(Student)
