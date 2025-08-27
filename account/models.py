from django.db import models
from django.contrib.auth.models
import User

class Customer(models.Model):
    name = models.CharField(max_length=100)
        email = models.EmailField(unique=True)
            phone = models.CharField(max_length=15)
            
            from django.db import models

            # Restaurant model to store basic info
            class Restaurant(models.Model):
                name = models.CharField(max_length=200)
                    description = models.TextField()
                        image = models.ImageField(upload_to='restaurant_images/', blank=True, null=True)

                            def __str__(self):
                                    return self.name
                                    
                                    class Menu(models.Model):
                                        name = models.CharField(max_length=100)
                                            description = models.TextField(blank=True, null=True)
                                                price = models.DecimalField(max_digits=6, decimal_places=2)

                                                    def __str__(self):
                                                            return self.name


                                                            class Order(models.Model):
                                                                STATUS_CHOICES = [
                                                                        ('pending', 'Pending'),
                                                                                ('completed', 'Completed'),
                                                                                        ('canceled', 'Canceled'),
                                                                                            ]

                                                                                                customer_name = models.CharField(max_length=100)
                                                                                                    total_amount = models.DecimalField(max_digits=8, decimal_places=2)
                                                                                                        status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
                                                                                                            created_at = models.DateTimeField(auto_now_add=True)

                                                                                                                def __str__(self):
                                                                                                                        return f"Order #{self.id} - {self.customer_name}"
 class Menu(models.Model):                                                                                                                       
        name = models.CharField(max_length=100)
            description = models.TextField(blank=True, null=True)
                price = models.DecimalField(max_digits=6, decimal_places=2)

                    def __str__(self):
                            return self.name


                            class Order(models.Model):
                                STATUS_CHOICES = [
                                        ('pending', 'Pending'),
                                                ('completed', 'Completed'),
                                                        ('canceled', 'Canceled'),
                                                            ]

                                                                customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
                                                                    total_amount = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
                                                                        status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
                                                                            created_at = models.DateTimeField(auto_now_add=True)

                                                                                def __str__(self):
                                                                                        return f"Order #{self.id} by {self.customer.username}"


                                                                                        class OrderItem(models.Model):
                                                                                            order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
                                                                                                menu_item = models.ForeignKey(Menu, on_delete=models.CASCADE)
                                                                                                    quantity = models.PositiveIntegerField(default=1)

                                                                                                        def __str__(self):
                                                                                                                return f"{self.quantity} × {self.menu_item.name} (Order #{self.order.id})"

                                                                                                                    def get_subtotal(self):
                                                                                                                            return self.menu_item.price * self.quantity
class Menu(models.Model):                                                                                                                            
        name = models.CharField(max_length=100)   # Dish name
            description = models.TextField()          # Dish description
                price = models.DecimalField(max_digits=6, decimal_places=2)  # e.g. 9999.99

                    def __str__(self):
                            return f"{self.name} - ${self.price}"
 class RestaurantLocation(models.Model):                           
        address = models.CharField(max_length=255)
            city = models.CharField(max_length=100)
                state = models.CharField(max_length=100)
                    zip_code = models.CharField(max_length=10)

                        def __str__(self):
                                return f"{self.address}, {self.city}, {self.state} {self.zip_code}"

class Contact(models.Model):                                
        name = models.CharField(max_length=100)
            email = models.EmailField()
                submitted_at = models.DateTimeField(auto_now_add=True)

                    def __str__(self):
                            return f"{self.name} - {self.email}"
class Menu(models.Model):                            
        name = models.CharField(max_length=100)
            description = models.TextField()
                price = models.DecimalField(max_digits=6, decimal_places=2)
                    image = models.ImageField(upload_to="menu_images/", blank=True, null=True)

                        def __str__(self):
                                return self.name
class Menu(models.Model):                                
        name = models.CharField(max_length=100)
            description = models.TextField()
                price = models.DecimalField(max_digits=6, decimal_places=2)
                    image = models.ImageField(upload_to="menu_images/", blank=True, null=True)

                        def __str__(self):
                                return self.name
  class RestaurantLocation(models.Model):                              
        address = models.CharField(max_length=255)
            city = models.CharField(max_length=100)
                state = models.CharField(max_length=100)
                    zip_code = models.CharField(max_length=20)

                        def __str__(self):
                                return f"{self.address}, {self.city}, {self.state} {self.zip_code}"
                                
                                class RestaurantLocation(models.Model):
                                    name = models.CharField(max_length=100)
                                        address = models.CharField(max_length=255, blank=True, null=True)
                                            opening_hours = models.JSONField(default=dict, blank=True, null=True)  # NEW FIELD

                                                def __str__(self):
                                                        return self.name