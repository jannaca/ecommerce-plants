from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateField(auto_now_add=True)
    total = models.DecimalField(default=0,max_digits=8,decimal_places=2)
    status = models.CharField(
    max_length=20,
    choices=[
        ('in_progress', 'En progreso'),
        ('completed', 'Completada'),
    ],
    default='in_progress',
    )
    cart_contents = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f"order #{self.id}"
    
    def clear_cart(self):
        self.products.clear()
        self.save()


