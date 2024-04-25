from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from api.models import Category, Product
from api.serializers import CategorySerializer, ProductSerializer
import json


class CategoryListAPIView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailAPIView(APIView):
    def get_object(self, category_id):
        try:
            category = Category.objects.get(id=category_id)
            return category
        except Category.DoesNotExist as e:
            return Response({'error': str(e)})

    def get(self, request, category_id):
        category = self.get_object(category_id)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, category_id):
        category = self.get_object(category_id)
        serializer = CategorySerializer(
            instance=category,
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()  # update table ...
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, category_id):
        category = self.get_object(category_id)
        category.delete()
        return Response({"deleted": True})

@csrf_exempt
def product_list(request):
    if request.method == "GET":
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        data = json.loads(request.body)
        product = Product.objects.create(name=data.get("name"), description=data.get("description"),
                                         rating=data.get("rating"))
        return JsonResponse(product.to_json(), status=201)


@csrf_exempt
def product_detail(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist as c:
        return JsonResponse({"error": str(c)}, status=400)

    if request.method == "GET":
        serializer = ProductSerializer(product)
        return JsonResponse(serializer.data)
    elif request.method == "PUT":
        data = json.loads(request.body)
        product.name = data.get("name")
        product.save()
    elif request.method == "DELETE":
        product.delete()
        return JsonResponse({"deleted": True})


@csrf_exempt
def category_products(request, category_id):
    try:
        products = Product.objects.all().filter(categoryId=category_id)
        products_json = [v.to_json() for v in products]
    except Category.DoesNotExist as exception:
        return JsonResponse({'exception': str(exception)}, status=400)
    return JsonResponse(products_json, safe=False)


