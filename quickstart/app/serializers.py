from .models import Employee 
from django.contrib.auth.models import User

from rest_framework import serializers


class  EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields= '__all__'

    
class  UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
