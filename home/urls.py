from django.urls import path
from . import views

urlpatterns = [
    path("contact/", views.contact_us, name="contact_us"),
]

urlpatterns = [
    path('', views.home, name='home'),
        path('reservations/', views.reservations, name='reservations'),
        ]