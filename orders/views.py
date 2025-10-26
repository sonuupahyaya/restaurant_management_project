from django.shortcuts import render
from .models import Order
from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer

class OrderDetailView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
        serializer_class = OrderSerializer
            lookup_field = 'order_id'  # use order_id instead of pk
            
def order_list(request):
    orders = Order.objects.select_related('customer', 'product')
        return render(request, 'orders/orders.html', {'orders': orders})
        