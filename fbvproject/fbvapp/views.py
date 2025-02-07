from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Course,CourseSerializar 
# Create your views here.




@api_view(['GET','POST'])
def CourseListView(request):
    if request.method == 'GET':
        course = Course.objects.all()
        courseserializar = CourseSerializar(course,Many = True)
        return Response(courseserializar.data)
    elif request.method == 'POST':
        courseserializar = CourseSerializar.objects.all()
        if courseserializar.is_valid():
            courseserializar.save()
            return (courseserializar.data)
        return (courseserializar.errors)
    
    
@api_view(['GET','PUT','DELETE'])    
def CourseDrtailView(request,pk):
    try: 
        course = Course.object.get(pk= pk)
    except Course.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        courseserializer = CourseSerializar(course)
        return Response(courseserializer.data)
    elif  request.method == 'PUT':
        courseserializer = CourseSerializar(course,data = request.data)
        if courseserializer.is_valid:
            courseserializer.save
            return (courseserializer.data)
        return (courseserializer.errors)
    elif  request.method == 'DELETE':
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)