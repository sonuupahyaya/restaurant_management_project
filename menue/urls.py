from django.urls import path
from .views import MenuItemsByCategoryView
# project/urls.py
from django.urls import path, include

urlpatterns = [
    path('api/', include('menu.urls')),
    ]
    
urlpatterns = [
    path('menu-items/', MenuItemsByCategoryView.as_view(), name='menu-items-by-category'),
    ]
