from rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    brand = serializers.CharField(max_length=100)
    description = serializers.TextField()
    price = serializers.FloatField()
    #image = serializers.ImageField()
    rating = serializers.FloatField()
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())