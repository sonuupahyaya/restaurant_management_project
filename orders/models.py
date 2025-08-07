from django.db import models
from account.models import Customer
from products.models import Product

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
        product = models.ForeignKey(Product, on_delete=models.CASCADE)
            quantity = models.PositiveIntegerField()
                date = models.DateTimeField(auto_now_add=True)
                