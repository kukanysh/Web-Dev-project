from django.urls import path, include

from api.views import *

urlpatterns = [
    path('products/', get_products),
    path('products/<int:pk>', get_product),
    path('categories/', get_categories),
    path('categories/<int:pk>',get_category),
    path('categories/<int:pk>/products', product_list_by_category)
]