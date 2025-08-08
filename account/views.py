from django.shortcuts import render
from .models import Customer

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
                 