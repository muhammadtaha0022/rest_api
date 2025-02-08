
from django.contrib import admin
from django.urls import path
from app.views import employeeListView,userListView , EmployeeDetailView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/employees/', employeeListView),
    path('api/employees/<int:pk>', EmployeeDetailView),
    path('api/user/', userListView)
]

