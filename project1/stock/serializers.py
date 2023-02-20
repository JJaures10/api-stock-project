
from django.contrib.auth.models import User
from rest_framework import serializers
from stock import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
   # category = CategorySerializer()
    class Meta:
        model = models.Product
        fields = '__all__'

