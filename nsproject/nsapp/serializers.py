from .models import Course,Instructor
from rest_framework import serializers



        
class InstructorSerializer(serializers.ModelSerializer):

    
    class Meta :
        model = Instructor
        fields = "__all__"
        
class CourseSerializer(serializers.ModelSerializer):
    instructor = InstructorSerializer(read_only = True)
    class Meta :
        model = Course
        fields = "__all__"
        