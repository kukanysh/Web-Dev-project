from rest_framework import serializers
from api.models import Category, Product

from backend.api.models import Cart


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    price = serializers.FloatField()
    description = serializers.CharField(max_length=255)
    category = CategorySerializer()


class OrderSerializer(serializers.Serializer):
    class Meta:
        model = Product
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer)
    class Meta:
        model = Product
        fields = '__all__'
