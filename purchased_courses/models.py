from django.db import models
from django.conf import settings

class PurchasedCourse(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey('courses.Courses', on_delete=models.CASCADE)  # Mengacu pada model Courses
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.course.title}"
