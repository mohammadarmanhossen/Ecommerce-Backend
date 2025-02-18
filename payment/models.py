from django.db import models
from product.models import Cart
from django.contrib.auth.models import User
from product.models import Cart

class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    start_date = models.DateField()
    out_date = models.DateField()  
    is_paid = models.BooleanField(default=False)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        if self.product and self.quantity:
            self.total_amount = self.product.price * self.quantity  
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.name} - {self.quantity} pcs"

    