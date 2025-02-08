from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Course, CourseSerializar
from rest_framework import status
from django.http import Http404
# Create your views here.

class CourseListView(APIView):
    def get(self,request):
        courses = Course.objects.all()
        serializer = CourseSerializar(courses , many = True)
        return Response(serializer.data)
    
    def post(self,request):
        courseserilizer = CourseSerializar(data = request.data)
        if courseserilizer.is_valid():
            courseserilizer.save()
            return Response(courseserilizer.data,status=status.HTTP_201_CREATED)
        return Response(CourseSerializar.errors)
    
    
class CourseDetailView(APIView):
    def get_course(self,pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            raise Http404
        
    def get(self ,request, pk):
        course = self.get_course(pk)
        serializer = CourseSerializar(course)
        return Response(serializer.data)
    def delete(self ,request, pk):
        self.get_course(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def put(self ,request, pk):
        course = self.get_course(pk)
        courseserializar = CourseSerializar(course , data=request.data)
        if courseserializar.is_valid():
            courseserializar.save()
            return Response(courseserializar.data)
        return Response(courseserializar.errors)