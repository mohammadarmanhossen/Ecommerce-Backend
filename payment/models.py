from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0) 
    is_paid = models.BooleanField(default=False)  


