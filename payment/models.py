from django.db import models
from product.models import Product

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1) 
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0) 
    is_paid = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.total_amount = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order for {self.product.name} (x{self.quantity})"



