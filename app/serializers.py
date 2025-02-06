from .models import Employee
from rest_framework import serializers


class  EmployeeSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    email = serializers.EmailField(max_length=254)
    password = serializers.CharField(max_length=50)
    phone = serializers.CharField(max_length=50)
    
    def create(selt,validated_data):
        print('create method fatima ')
        return Employee.objects.create(**validated_data)
    
    def update(self, employee, validated_data):
        newemployee = Employee(**validated_data)
        newemployee.id = employee.id
        newemployee.save()
        return newemployee
    
class  UserSerializers(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    email = serializers.EmailField(max_length=254)
    password = serializers.CharField(max_length=50)