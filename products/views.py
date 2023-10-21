from django.shortcuts import render
from .models import Product

def index(request):
    products = Product.objects.all() #Listar todos los productos del modelo
    
    return render( request, # solicitud HTTP que se pasa a la vista.
                   "products/index.html", # plantilla HTML que se utilizará para renderizar la respuesta
                  { "products": products }) # diccionario que contiene datos que se pasan a la plantilla

def get_product(request,id):
    product = Product.objects.get(id=id) #obtener el id del producto que se pasa por parametro

    return render( request, 
                   "products/show_product.html", 
                  { "product": product }) 