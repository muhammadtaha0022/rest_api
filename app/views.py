from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Employee
from .serializers import EmployeeSerializers,UserSerializers
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status

@csrf_exempt
def employeeListView(request):
    if request.method == 'GET':
        employee = Employee.objects.all()
        serializer = EmployeeSerializers(employee,many = True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method =='POST': 
        jsondata = JSONParser().parse(request)
        serializer = EmployeeSerializers(data =jsondata)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, sefe= False)
        else:
            return JsonResponse(serializer.errors,safe= False)
            
        # return JsonResponse(serializer.data,safe=False)  
        
@csrf_exempt
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
        return JsonResponse(serializer.data , safe =False)
        
    elif request.method == 'PUT':
        jsondata = JSONParser().parse(request)
        serializer = EmployeeSerializers(employee, data =jsondata)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, sefe= False)
        else:
            return JsonResponse(serializer.errors,safe= False)    

        
def userListView(request):
        users = User.objects.all()
        serializer = UserSerializers(users,many= True)
        return JsonResponse(serializer.data,safe= False)