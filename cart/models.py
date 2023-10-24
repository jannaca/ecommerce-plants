from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from products.models import Product

class Cart(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    order_status = models.CharField(max_length=50, default="pending")
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(default=timezone.now)
