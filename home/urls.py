from django.urls import path
from .views import TableDetailView
# project/urls.py
from django.urls import path, include
from django.urls import path
from .views import AvailableTablesAPIView

urlpatterns = [
    path('api/tables/available/', AvailableTablesAPIView.as_view(), name='available_tables_api'),
    ]
    
urlpatterns = [
    path('', include('home.urls')),  # Make sure 'home' app is included
    ]
    
urlpatterns = [
    # Example: http://127.0.0.1:8000/api/tables/1/
        path('api/tables/<int:pk>/', TableDetailView.as_view(), name='table-detail'),
        ]
