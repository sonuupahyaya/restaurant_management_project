from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
        address = models.TextField()
            phone_number = models.CharField(max_length=15)
                email = models.EmailField()
                    operating_days = models.CharField(
                            max_length=100,
                                    help_text="Enter days like: Mon,Tue,Wed,Thu,Fri,Sat,Sun"
                                        )

                                            def __str__(self):
                                                    return self.name
                                                    