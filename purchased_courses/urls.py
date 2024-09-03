from django.urls import path
from .views import PurchasedCourseListView

urlpatterns = [
    path('my-courses/', PurchasedCourseListView.as_view(), name='my_courses'),
]
