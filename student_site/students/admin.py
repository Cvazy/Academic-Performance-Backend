from django.contrib import admin
from student_site.students.models import *

# Register your models here.
model_list = [Student, Discipline, Speciality, Group, AcademicPerformance]
admin.site.register(model_list)