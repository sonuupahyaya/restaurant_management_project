
    # home/views.py
    from django.http import HttpResponse
    from django.shortcuts import render
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