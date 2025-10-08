from django.db import models
from account.models import Customer
from products.models import Product

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)
                from django.db import models

                
                    name = models.CharField(max_length=50, unique=True)

                        def __str__(self):
                                return self.name
from django.db import models

# Assuming OrderStatus is already defined
from .models import OrderStatus

class Order(models.Model):
    # Existing fields
        user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
            total_amount = models.DecimalField(max_digits=10, decimal_places=2)
                created_at = models.DateTimeField(auto_now_add=True)
                    
                        # Add this field to track order status
                            status = models.ForeignKey(OrderStatus, on_delete=models.SET_NULL, null=True)

                                def __str__(self):
                                        return f"Order {self.id} - {self.user.username}"
                                        