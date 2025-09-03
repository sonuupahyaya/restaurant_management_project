
    # home/views.py
    from django.http import HttpResponse
    from .models import Menu
    from django.shortcuts import render
    from import datetime import datetime
    def homepage(request):
        return HttpResponse("""
    <html>
    <head>
        <title>Welcome to Restaurant Menu API</title>
    </head>
    <body style="font-family: Arial, sans-serif; background-color: #f4f4f4; margin: 0; padding: 0;">
    <div style="max-width: 800px; margin: 50px auto; background: white; padding: 20px; border-radius: 10px; box-shadow: 0px 4px 8px rgba(0,0,0,0.1); text-align: center;">
        <h1 style="color: #2c3e50; font-size: 2.5rem;">🍽️ Welcome to Restaurant Menu API</h1>
        <p style="font-size: 1.2rem; color: #555;">
        Explore our menu and discover delicious dishes served fresh every day!
        </p>
        <a href="/api/" style="display: inline-block; margin-top: 15px; padding: 10px 20px; background: #27ae60; color: white; text-decoration: none; border-radius: 5px; font-weight: bold;">
            View API Endpoints
        </a>
    </div>
    </body>
    </html>
              """)
    def home_view(request):
        return render(request, "home.html")

    def contact_us(request):    
            """
            Render the Contact Us page with hardcoded contact details.
            """
            contact_info = {
                "company_name": "Delicious Bites Restaurant",
                "phone": "+91 98765 43210",
                "email": "contact@deliciousbites.com",
                "address": "123 Main Street, Mumbai, India"
            }
            return render(request, "contact_us.html", {"contact": contact_info})

def home(request):
    return render(request, "home.html", {
            "restaurant_name": "My Restaurant",
                    "phone_number": "+91 98765 43210",
                            "current_year": datetime.now().year
                                })

def reservations(request):
    return render(request, "reservations.html", {
            "restaurant_name": "My Restaurant",
                    "phone_number": "+91 98765 43210",
                            "current_year": datetime.now().year
                                })
def home(request):                                
        menu_items = Menu.objects.all()  # fetch menu from DB
            return render(request, "home.html", {"menu_items": menu_items})
            