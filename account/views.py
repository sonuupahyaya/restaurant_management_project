from django.shortcuts import render
from django.shortcuts import render, redirect
from .form import ContactForm
from .models import Customer
from django.shortcuts import
from .models import Menue
from .models import RestaurantLocation
from django.conf import settings
from django.shortcuts import render
from .models import RestaurantLocation

def home(request):
    location = RestaurantLocation.objects.first()
        return render(request, "home.html", {"location": location})
        
def customer_list(request):
    customers = Customer.objects.all()
        return render(request, 'account/customers.html', {'customers': customers})
            
            from django.shortcuts import render
            from django.conf import settings  # to access settings.py variables

            def home(request):
                """
                    View to display the homepage with restaurant name fetched from settings.py
                        """
                            restaurant_name = getattr(settings, 'RESTAURANT_NAME', 'Our Restaurant')  # default if not found
                                
                                    return render(request, 'home.html', {
                                            'restaurant_name': restaurant_name
                                                })
                                                
 from django.shortcuts import render                                               
 from .models import Restaurant

 # Homepage view
 def home(request):
     restaurant = Restaurant.objects.first()
         return render(request, 'home/index.html', {'restaurant': restaurant})

         # About page view
         def about(request):
             restaurant = Restaurant.objects.first()
                 return render(request, 'home/about.html', {'restaurant': restaurant})
def home(request):                 
        restaurant_name = getattr(settings, "RESTAURANT_NAME", "My Restaurant")
            return render(request, "home.html", {"restaurant_name": restaurant_name})
 def menu_view(request):           
        """
            Display all menu items on a dedicated menu page.
                """
                    menu_items = Menu.objects.all().order_by("name")  # fetch all, order by name
                        return render(request, "menu.html", {"menu_items": menu_items})
 render, redirect                       
 from .forms import ContactForm

 def homepage(request):
     restaurant_name = getattr(settings, "RESTAURANT_NAME", "My Restaurant")
         phone_number = getattr(settings, "RESTAURANT_PHONE", "+91 99999 99999")
             address = getattr(settings, "RESTAURANT_ADDRESS", "Address not set")

                 if request.method == "POST":
                         form = ContactForm(request.POST)
                                 if form.is_valid():
                                             form.save()  # Save to database
                                                         return redirect("homepage")  # Redirect to avoid resubmission
                                                             else:
                                                                     form = ContactForm()

                                                                         return render(request, "homepage.html", {
                                                                                 "restaurant_name": restaurant_name,
                                                                                         "phone_number": phone_number,
                                                                                                 "address": address,
                                                                                                         "form": form,
                                                                                                             })
 def contact_view(request):                                                                                                            
        if request.method == "POST":
                form = ContactForm(request.POST)
                        if form.is_valid():
                                    form.save()
                                                return redirect("contact")  # reload page after submission
                                                    else:
                                                            form = ContactForm()

                                                                return render(request, "contact.html", {"form": form})
def menu_view(request):                                                                
        items = Menu.objects.all()
            return render(request, "menu.html", {"items": items})
def home(request):            
        location = RestaurantLocation.objects.first()  # get the first saved address
            return render(request, "home.html", {"location": location})
            