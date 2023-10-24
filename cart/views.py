from django.shortcuts import render, redirect
from .models import Cart, Product

def add_to_cart(request, product_id):
    # Obtén el producto que se desea agregar al carrito
    product = Product.objects.get(id=product_id)
    
    # Verifica si el usuario ya tiene un carrito o necesita crear uno
    user = request.user
    cart, created = Cart.objects.get_or_create(id_user=user)

    cartItems = cart.Cart.all()