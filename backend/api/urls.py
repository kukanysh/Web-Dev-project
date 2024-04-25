from django.contrib import admin
from django.urls import path
from api.views import CategoryListAPIView, CategoryDetailAPIView, ProductListAPIView, ProductDetailAPIView
from api.views import category_products

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view()),
    path('categories/<int:category_id>/', CategoryDetailAPIView.as_view()),
    path('categories/<int:category_id>/products', category_products),
    path('products/', ProductListAPIView.as_view()),
    path('products/<int:product_id>/', ProductDetailAPIView.as_view()),
]