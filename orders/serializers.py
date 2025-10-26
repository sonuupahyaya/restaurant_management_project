from rest_framework import serializers
from .models import Order
from account.models import Customer
from home.models import MenuItem

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
            model = Customer
                    fields = ['id', 'name', 'email']  # include fields as per your model

                    class MenuItemSerializer(serializers.ModelSerializer):
                        class Meta:
                                model = MenuItem
                                        fields = ['id', 'name', 'price']

                                        class OrderSerializer(serializers.ModelSerializer):
                                            customer = CustomerSerializer(read_only=True)
                                                items = MenuItemSerializer(many=True, read_only=True)

                                                    class Meta:
                                                            model = Order
                                                                    fields = ['order_id', 'customer', 'items', 'total_price', 'order_date']
                                                                    