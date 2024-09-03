from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import PurchasedCourse
from .serializers import PurchasedCourseSerializer

class PurchasedCourseListView(generics.ListAPIView):
    serializer_class = PurchasedCourseSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = None  

    def get_queryset(self):
        return PurchasedCourse.objects.filter(user=self.request.user)
