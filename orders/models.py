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
class Coupon(models.Model):                                        
        code = models.CharField(max_length=50, unique=True)
            discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
                is_active = models.BooleanField(default=True)
                    valid_from = models.DateField()
                        valid_until = models.DateField()

                            def __str__(self):
                                    return self.code

                                        def is_valid(self):
                                                today = timezone.now().date()
                                                        return self.is_active and self.valid_from <= today <= self.valid_until
# menu/models.py                                                        


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
        description = models.TextField(blank=True)
            price = models.DecimalField(max_digits=8, decimal_places=2)
                is_available = models.BooleanField(default=True)

                    def __str__(self):
                            return self.name
