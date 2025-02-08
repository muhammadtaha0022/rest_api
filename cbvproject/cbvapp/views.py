from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Course, CourseSerializar
from rest_framework import status
from django.http import Http404
# Create your views here.
from rest_framework import mixins,generics
from rest_framework.viewsets import ViewSet



class CourseViewSet(ViewSet):
    def list(self , request):
        courses = Course.objects.all()
        serializer = CourseSerializar(courses, many = True)
        return Response(serializer.data)
    
    def retrive(self,request,pk):
        try:
            course = Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CourseSerializar(course)
        return Response(serializer.data)




# class CourseListView(generics.ListCreateAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializar


# class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializar


# class CourseListView(generics.ListAPIView, generics.CreateAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializar

# class CourseDetailView(generics.RetrieveAPIView,generics.UpdateAPIView,generics.DestroyAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializar


# class CourseListView(mixins.ListModelMixin, mixins.CreateModelMixin,generics.GenericAPIView):
    # queryset = Course.objects.all()
    # serializer_class = CourseSerializar
    # def get(self,request):
    #     return self.list(request)
    # def post(self,request):
    #     return self.create(request)
  
    
# class CourseDetailView(generics.GenericAPIView, mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializar
    
#     def get(self,request,pk):
#         return self.retrieve(request,pk)
    
#     def put(self,request, pk):
#         return self.update(request,pk)
    
#     def delete(self ,request, pk):
#         return self.destroy(request,pk) 












# class CourseListView(APIView):
#     def get(self,request):
#         courses = Course.objects.all()
#         serializer = CourseSerializar(courses , many = True)
#         return Response(serializer.data)
    
#     def post(self,request):
#         courseserilizer = CourseSerializar(data = request.data)
#         if courseserilizer.is_valid():
#             courseserilizer.save()
#             return Response(courseserilizer.data,status=status.HTTP_201_CREATED)
#         return Response(CourseSerializar.errors)
    
    
# class CourseDetailView(APIView):
#     def get_course(self,pk):
#         try:
#             return Course.objects.get(pk=pk)
#         except Course.DoesNotExist:
#             raise Http404
        
#     def get(self ,request, pk):
#         course = self.get_course(pk)
#         serializer = CourseSerializar(course)
#         return Response(serializer.data)
#     def delete(self ,request, pk):
#         self.get_course(pk).delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     def put(self ,request, pk):
#         course = self.get_course(pk)
#         courseserializar = CourseSerializar(course , data=request.data)
#         if courseserializar.is_valid():
#             courseserializar.save()
#             return Response(courseserializar.data)
#         return Response(courseserializar.errors)