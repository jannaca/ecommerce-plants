from django.shortcuts import render,redirect, get_object_or_404

from .models import CartItem
from products.models import Product
from .utils import get_or_created_cart

def view_cart(request):
    cart = get_or_created_cart(request)
  
    return render(request, "cart/cart.html", {"cart":cart})


def add_to_cart(request):
    cart = get_or_created_cart(request)
    product = get_object_or_404(Product, pk=request.POST.get("product_id"))
    quantity = int(request.POST.get("quantity", 1))
    
    # cart.products.add(product, through_defaults={
    #     "quantity": quantity
    # })
    cart_item = CartItem.objects.create_or_update_quantity(cart= cart, 
                                                            product = product, 
                                                            quantity = quantity)
    return render( request, 
                  "cart/add.html", 
                  {"product": product
    })

def remove_to_cart(request):
    cart = get_or_created_cart(request)
    product = get_object_or_404(Product, pk=request.POST.get("product_id"))

    cart.products.remove(product)

    return redirect("cart")