from django.shortcuts import render
from carts.utils import get_or_created_cart
from .utils import get_or_create_order

def create_order(request):
    cart = get_or_created_cart(request)
    cart_contents = {'products': [{'id': item.product.id, 'quantity': item.quantity} for item in cart.cartitem_set.all()],}
    total = cart.total
    order = get_or_create_order(cart_contents, total, request)
    cart.clear_cart()
    return render(request,
           "orders/orders.html",
           {"order": order})


