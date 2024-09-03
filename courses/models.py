# courses/models.py
from django.db import models

class Courses(models.Model):
    CATEGORY_CHOICES = [
        ('informasi-teknologi', 'Informasi Teknologi'),
        ('marketing', 'Marketing'),
        ('bisnis', 'Bisnis'),
    ]

    title = models.CharField(max_length=255)
    instructor = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    is_verified = models.BooleanField(default=False)
    rating = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField()  # URL gambar di MinIO

    def __str__(self):
        return self.title
