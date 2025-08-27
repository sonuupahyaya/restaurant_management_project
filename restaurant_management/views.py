from django.shortcuts import render
from .models import RestaurantLocation

def home(request):
    location = RestaurantLocation.objects.first()
        context = {"location": location}
            return render(request, "home.html", context)
            