from rest_framework import viewsets

# For json data
from .serializers import CategorySerializer

# Model we created
from .models import Category

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer