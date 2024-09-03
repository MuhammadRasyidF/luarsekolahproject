# courses/views.py
from minio import Minio
from minio.error import S3Error
from django.conf import settings
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Courses
from .serializers import CoursesSerializer

# Initialize MinIO client
minio_client = Minio(
    endpoint=settings.MINIO_ENDPOINT,
    access_key=settings.MINIO_ACCESS_KEY,
    secret_key=settings.MINIO_SECRET_KEY,
    secure=False
)

@api_view(['POST'])
def create_course(request):
    file = request.FILES.get('image')
    if not file:
        return Response({"error": "Image file is required"}, status=status.HTTP_400_BAD_REQUEST)

    bucket_name = settings.MINIO_BUCKET_NAME
    file_key = f'courses/{file.name}'  # Path in MinIO bucket
    
    # Upload file to MinIO
    try:
        minio_client.put_object(bucket_name, file_key, file, file.size)
    except S3Error as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    file_url = f'http://{settings.MINIO_ENDPOINT}/{bucket_name}/{file_key}'

    print(file_url)
    serializer = CoursesSerializer(data={
        'title': request.data.get('title'),
        'instructor': request.data.get('instructor'),
        'category': request.data.get('category'),
        'is_verified': request.data.get('is_verified'),
        'rating': request.data.get('rating'),
        'price': request.data.get('price'),
        'image_url': file_url
    })

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_courses(request):
    category = request.query_params.get('category')
    if category:
        courses = Courses.objects.filter(category=category)
    else:
        courses = Courses.objects.all()
    
    serializer = CoursesSerializer(courses, many=True)
    return Response(serializer.data)
