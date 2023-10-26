from .models import Cart


def get_or_created_cart(request):
    user = request.user
    cart = None

    if user.is_authenticated:
        # Si el usuario está autenticado, obtén su carrito (si existe)
        cart, created = Cart.objects.get_or_create(user=user)
    else:
        # Si el usuario no está autenticado, usa el carrito basado en la sesión
        cart_id = request.session.get("cart_id")
        if cart_id:
            cart = Cart.objects.filter(cart_id=cart_id).first()

        if cart is None:
            cart = Cart.objects.create()

        # Asigna el carrito a la sesión para futuras solicitudes
        request.session["cart_id"] = cart.cart_id

    return cart