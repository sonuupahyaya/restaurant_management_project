from django.shortcuts import render
from .models import Order

def order_list(request):
    orders = Order.objects.select_related('customer', 'product')
        return render(request, 'orders/orders.html', {'orders': orders})
        