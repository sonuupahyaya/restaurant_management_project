from django.db import models

# Create your models here.
from django.db import models
from django.db import models

class Table(models.Model):
    table_number = models.IntegerField(unique=True)
        seating_capacity = models.IntegerField()
            status = models.CharField(max_length=20, default="Available")  # e.g., Available / Reserved

                def __str__(self):
                        return f"Table {self.table_number}"
                        
class MenuCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

        def __str__(self):
                return self.name
                