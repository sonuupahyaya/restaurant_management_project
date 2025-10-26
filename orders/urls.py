from django.urls import path
from . import views
from django.urls import path
from .views import OrderDetailView

urlpatterns = [
    path('<int:order_id>/', OrderDetailView.as_view(), name='order-detail'),
    ]
    
urlpatterns = [
    path('orders/', views.order_list, name='order_list'),
    ]


    menu_search = MenuItemSearchViewSet.as_view({'get': 'list'})

    urlpatterns = [
        path('menu/search/', menu_search, name='menu-search'),
        ]
