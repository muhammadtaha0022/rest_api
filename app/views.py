from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Employee
from .serializers import EmployeeSerializers,UserSerializers
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET','POST'])
def employeeListView(request):
    if request.method == 'GET':
        employee = Employee.objects.all()
        serializer = EmployeeSerializers(employee,many = True)
        return Response(serializer.data)
    elif request.method =='POST': 
        serializer = EmployeeSerializers(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
            
        # return Response(serializer.data,safe=False)  
        
@api_view(['DELETE', 'GET', 'PUT'])
def EmployeeDetailView(request , pk):
    try:
        employee = Employee.objects.get(pk=pk)
        
    except Employee.DoesNotExist:
        return HttpResponse(status= 404)
    
     
    if request.method == 'DELETE':
        employee.delete()
        return HttpResponse(status = status.HTTP_204_NO_CONTENT )
    elif request.method == 'GET':
        serializer = EmployeeSerializers(employee)
        return Response(serializer.data)
        
    elif request.method == 'PUT':
        serializer = EmployeeSerializers(employee, data =Response.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, sefe= False)
        else:
            return Response(serializer.errors)    

@api_view(['GET'])  
def userListView(request):
        if request.method == 'GET':
            users = User.objects.all()
            serializer = UserSerializers(users,many= True)
            return Response(serializer.data)