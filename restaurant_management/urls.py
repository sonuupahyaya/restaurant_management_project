from django.contrib import admin
from django.urls import path, include
from home.Views import home_view

urlpatterns = [
    path('products/',include('products.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('home.urls')),
    path('api/accounts/', include('account.urls')),
    path('api/products/', include('products.urls')),
    path('api/orders/', include('orders.urls')),
]


# Custom 404 error handler (points to a view in the 'home' app)
handler404 = 'home.views.custom_404_view'

