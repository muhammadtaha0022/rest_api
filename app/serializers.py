from .models import Employee
from rest_framework import serializers


class  EmployeeSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    email = serializers.EmailField(max_length=254)
    password = serializers.CharField(max_length=50)
    phone = serializers.CharField(max_length=50)