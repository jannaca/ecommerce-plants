from django.db import models

from django.utils import timezone

class Product(models.Model):
    name  = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to="media/products")
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name #Devuelve el nombre del producto en el panel de admin
