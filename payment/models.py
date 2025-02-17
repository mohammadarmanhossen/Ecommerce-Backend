from django.db import models
from product.models import Cart
from django.contrib.auth.models import User
from product.models import Cart

class Checkout(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE, related_name="checkouts", default=1)
    def __str__(self):  
        return self.name
    

    