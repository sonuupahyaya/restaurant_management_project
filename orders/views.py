from django.shortcuts import render
from .models import Order
from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer
from .utils import send_order_confirmation_email

class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
        serializer_class = OrderSerializer

            def perform_create(self, serializer):
                    order = serializer.save()

                            # Extract details for email
                                    customer_name = order.customer.name
                                            customer_email = order.customer.email
                                                    order_id = order.order_id
                                                            total_price = order.total_price
                                                                    items_list = [item.name for item in order.items.all()]

                                                                            # Send confirmation email
                                                                                    result = send_order_confirmation_email(order_id, customer_email, customer_name, total_price, items_list)
                                                                                            if not result["success"]:
                                                                                                        # Optionally log or return error response if email fails
                                                                                                                    print(result["message"])
                                                                                                                    
class OrderDetailView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
        serializer_class = OrderSerializer
            lookup_field = 'order_id'  # use order_id instead of pk
            
def order_list(request):
    orders = Order.objects.select_related('customer', 'product')
        return render(request, 'orders/orders.html', {'orders': orders})
        