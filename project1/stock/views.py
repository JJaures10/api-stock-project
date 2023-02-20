from django.shortcuts import render

from rest_framework import viewsets, filters, permissions
from stock.models import *
from stock.serializers import *

# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):    
    queryset = Category.objects.all()
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields =("name",)
    serializer_class = CategorySerializer
    

class ProductViewSet(viewsets.ModelViewSet):    
    queryset = Product.objects.all()
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields =("name",)
    serializer_class = ProductSerializer

class UserViewSet(viewsets.ModelViewSet):    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]