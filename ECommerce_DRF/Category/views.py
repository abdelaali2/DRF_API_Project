from django.shortcuts import render
from .models import Category
from rest_framework import generics
from .serializers import CategorySerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
