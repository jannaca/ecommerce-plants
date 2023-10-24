from django.urls import path
from .views import add_to_cart


urlpatterns = [
    # Otras rutas...
    path('agregar-al-carrito/<int:product_id>/', add_to_cart, name='add_to_cart'),
#     path('carrito/', views.view_cart, name='carrito'),  # Reemplaza 'view_cart' con el nombre de tu vista para ver el carrito
#     # Otras rutas...
]


