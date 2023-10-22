from django.contrib import admin
from django.urls import path
from .views import index, get_product, shop

urlpatterns = [
    path('', index, name="index"),
    path('product/<int:id>', get_product, name='get_product'),
    path("tienda/categorias",shop,name="shop"),
    path("tienda/categorias/<int:category_id>",shop,name="shop_categories")
]
