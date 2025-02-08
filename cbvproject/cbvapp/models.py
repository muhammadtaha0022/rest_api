from django.db import models
from rest_framework import serializers
# Create your models here.
class Course(models.Model):
    name = models.CharField( max_length=50)
    author = models.CharField(max_length=50)
    price = models.IntegerField()
    discount = models.IntegerField()
    duration = models.FloatField()
    
class CourseSerializar(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'