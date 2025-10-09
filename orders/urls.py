from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.order_list, name='order_list'),
    ]


    menu_search = MenuItemSearchViewSet.as_view({'get': 'list'})

    urlpatterns = [
        path('menu/search/', menu_search, name='menu-search'),
        ]
