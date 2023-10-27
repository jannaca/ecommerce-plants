from django.shortcuts import render
from carts.utils import get_or_created_cart
from .utils import get_or_create_order

def create_order(request):
    cart = get_or_created_cart(request)
    order = get_or_create_order(cart,request)
    return render(request,
           "orders/orders.html",
           {"order":order})


