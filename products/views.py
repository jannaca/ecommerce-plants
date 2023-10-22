from django.shortcuts import render
from .models import Product, Category

def index(request):
    last_products = Product.objects.order_by('-created_date')[:3] #Obtener los ultimos 3 productos añadidos
    
    return render( request, # solicitud HTTP que se pasa a la vista.
                   "products/index.html", # plantilla HTML que se utilizará para renderizar la respuesta
                  { "products": last_products }) # diccionario que contiene datos que se pasan a la plantilla

def get_product(request,id):
    product = Product.objects.get(id=id) #obtener el id del producto que se pasa por parametro

    return render( request, 
                   "products/show_product.html", 
                  { "product": product }) 

def shop(request,category_id=None):
    categories = Category.objects.all()
    category_description = None
    categories_filter = None
    if category_id is not None:
        categories_filter = Category.objects.get(id=category_id)
        products_filter = Product.objects.filter(categories=categories_filter)
        category_description = categories_filter.description
    else:
        products_filter = Product.objects.all()
    return render(
        request,
        "products/shop.html",
        {"categories": categories,"products":products_filter, "category_description": category_description,"categories_filter": categories_filter}
    )