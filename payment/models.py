from django.db import models
from product.models import Cart
from django.contrib.auth.models import User
from product.models import Product

class Checkout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ManyToManyField(Cart)
    Order = models.BooleanField(default=False)  
    total_amount = models.DecimalField(max_digits=7, decimal_places=2)
    tran_id = models.CharField(max_length=100, blank=True, null=True)

    
    def __str__(self):  
        return self.name
    
class OrderdItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    buyer_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField( blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(blank=True, null=True)
    buying_time = models.DateTimeField(auto_now_add=True)
    tran_id = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.user.username} - {self.product.name}"
    