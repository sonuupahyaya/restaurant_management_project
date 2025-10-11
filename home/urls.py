from django.urls import path
from .views import TableDetailView
# project/urls.py
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),  # Make sure 'home' app is included
    ]
    
urlpatterns = [
    # Example: http://127.0.0.1:8000/api/tables/1/
        path('api/tables/<int:pk>/', TableDetailView.as_view(), name='table-detail'),
        ]
