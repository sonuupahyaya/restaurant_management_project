from rest_framework import serializers
from .models import MenuCategory
from rest_framework import serializers
from .models import Table

class TableSerializer(serializers.ModelSerializer):
    class Meta:
            model = Table
                    fields = ['table_number', 'capacity', 'is_available']
                    
class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
            model = MenuCategory
                    fields = ['name']  # Only include the name field
                   

                    class MenuItemSerializer(serializers.ModelSerializer):
                        class Meta:
                                model = MenuItem
                                        fields = ['id', 'name', 'description', 'price', 'is_available']

                                            def validate_price(self, value):
                                                    if value <= 0:
                                                                raise serializers.ValidationError("Price must be a positive number.")
                                                                        return value
