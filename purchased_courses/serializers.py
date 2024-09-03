from rest_framework import serializers
from .models import PurchasedCourse

class PurchasedCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchasedCourse
        fields = ['id', 'user', 'course', 'purchase_date']
