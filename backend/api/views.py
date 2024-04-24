from django.shortcuts import render

# Create your views here.
from django.http.response import JsonResponse
from django.core.serializers import serialize

from api.models import Product
from api.models import Category


def get_products(request):
    products = Product.objects.all()
    products_json = serialize('json', products)

    return JsonResponse(products_json, safe=False)


def get_product(request, pk=None):
    try:
        product = Product.objects.get(id=pk)
        product_json = serialize('json', [product])
        return JsonResponse(product_json, safe=False)
    except Product.DoesNotExist as e:
        return JsonResponse({
            'error': str(e)
        })


def get_categories(request):
    categories = Category.objects.all()
    category_json = serialize('json', categories)

    return JsonResponse(category_json, safe=False)


def get_category(request, pk=None):
    try:
        category = Category.objects.get(id=pk)
        category_json = serialize('json', [category])
        return JsonResponse(category_json, safe=False)
    except Category.DoesNotExist as e:
        return JsonResponse({
            'error': str(e)
        })

def product_list_by_category(request, pk):
    try:
        products = Product.objects.filter(category_id=pk)
        products_json = serialize('json', products)
        return JsonResponse(products_json, safe=False)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'No products found for this category'}, status=404)
