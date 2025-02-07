from django.contrib import admin
from django.urls import path
from .views import CourseListView,CourseDrtailView
urlpatterns = [
    path('courses/', CourseListView),
    path('courses/<int:pk>', CourseDrtailView),
]
