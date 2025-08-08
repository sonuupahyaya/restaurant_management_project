from django.db import models

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
                                    