from django.shortcuts import render
from .models import Product

def index(request):
    products = Product.objects.all() #Listar todos los productos del modelo
    
    return render( request, # solicitud HTTP que se pasa a la vista.
                   "index.html", # plantilla HTML que se utilizará para renderizar la respuesta
                  { "products": products }) # diccionario que contiene datos que se pasan a la plantilla