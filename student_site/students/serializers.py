from rest_framework.serializers import ModelSerializer
from student_site.students.models import *


class StudentSerializer(ModelSerializer):
    
    class Meta:
        model = Student
        fields = '__all__'


class GroupSerializer(ModelSerializer):
    
    class Meta:
        model = Group
        fields = '__all__'


class SpecialitySerializer(ModelSerializer):
    
    class Meta:
        model = Speciality
        fields = '__all__'


class DisciplineSerializer(ModelSerializer):
    
    class Meta:
        model = Discipline
        fields = '__all__'
