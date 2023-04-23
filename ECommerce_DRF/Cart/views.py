from django.shortcuts import render
from .models import Cart
from rest_framework import generics
from .serializers import CartSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class CartList(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]
