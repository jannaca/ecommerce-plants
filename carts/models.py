import uuid
from django.db import models
from products.models import Product
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, m2m_changed, post_save
from collections import defaultdict

class Cart(models.Model):
    cart_id = models.CharField(max_length=100,null =False, blank =False, unique= True, default='')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through= "CartItem")
    total = models.DecimalField(default=0.0, max_digits=8,decimal_places=2)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id
    
    def update_totals(self):
        total = sum([
            cp.quantity * cp.product.price for cp in self.cartitem_set.select_related("product")
        ])
        self.total = total
        # order = self.order_set.first()
        # if order:
        #     order.update_total()
        self.save()

    def products_related(self):
        return self.cartitem_set.select_related("product")
    
    def clear_cart(self):
        self.products.clear()

    def get_cart_contents(self):
        cart_contents = {}  # Un diccionario para almacenar productos y cantidades
        cart_items = self.cartitem_set.all()  # Suponiendo que tienes un modelo CartItem relacionado con Cart

        for item in cart_items:
            product_id = item.product.id  # Obtener el ID del producto
            quantity = item.quantity  # Suponiendo que tienes un campo "quantity" en tu modelo CartItem
            cart_contents[product_id] = quantity

        return cart_contents

class CartProductsManager(models.Manager):
    def create_or_update_quantity(self, cart,product,quantity=1):
        object, created = self.get_or_create(cart=cart,product=product)

        if not created:
            quantity = object.quantity + quantity

        object.update_quantity(quantity)
        return object
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_at = models.DateField(auto_now_add=True)

    objects= CartProductsManager()
    
    def update_quantity(self,quantity=1):
        self.quantity =quantity
        self.save()

def set_cart_id(sender, instance, *args, **kwargs):
    if not instance.cart_id:
        instance.cart_id = str(uuid.uuid4())

def update_totals(sender, instance, action, *args, **kwargs):
    if action == "post_add" or action == "post_remove" or action == "post_clear":    
        instance.update_totals()

def post_save_update_totals(sender,instance, *args, **kwargs):
    instance.cart.update_totals() 

pre_save.connect(set_cart_id, sender=Cart)
post_save.connect(post_save_update_totals, sender=CartItem)
m2m_changed.connect(update_totals, sender=Cart.products.through )