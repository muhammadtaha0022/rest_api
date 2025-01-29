from django.shortcuts import render
from django.http import JsonResponse
from .models import Employee
from .serializers import EmployeeSerializers

def employeeListView(request):
    employee = Employee.objects.all()
    serializer = EmployeeSerializers(employee,many = True)
    return JsonResponse(serializer.data,safe=False)