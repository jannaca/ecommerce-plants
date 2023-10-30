from .models import Order
import json

def get_or_create_order(cart_contents, total, request):
    order = Order.objects.filter(status='in_progress').first()
    
    if not order and request.user.is_authenticated:
        order = Order.objects.create(user=request.user, status='completed')

    if order:
        # Almacena el contenido del carrito en el campo 'cart_contents' como JSON
        order.cart_contents = json.dumps(cart_contents)
        
        # Actualiza el campo 'total' de la orden
        order.total = total
        order.save()

    return order

