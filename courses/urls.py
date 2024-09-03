# courses/urls.py
from django.urls import path
from .views import create_course, list_courses

urlpatterns = [
    path('add/', create_course, name='create_course'),
    path('', list_courses, name='list_courses'),
]
