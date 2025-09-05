from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
        price = models.DecimalField(max_digits=8, decimal_places=2)
            available = models.BooleanField(default=True)
            class Restaurant(models.Model):
                    name = models.CharField(max_length=100)
                        address = models.TextField()
                            phone_number = models.CharField(max_length=15, blank=True, null=True)  # NEW field
                                logo = models.ImageField(upload_to="logos/", blank=True, null=True)

                                    def __str__(self):
                                            return self.name
                                            