from django.contrib import admin
from django.urls import path, include
from home.Views import home_view
from django.conf.urls.static import static
from django.urls import path, include
from django.conf.urls.static import
from django.conf.import settings
urlpatterns = [
    path('products/',include('products.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('home.urls')),
    path('api/accounts/', include('account.urls')),
    path('api/products/', include('products.urls')),
    path('api/orders/', include('orders.urls')),
]


# Custom 404 error handler (points to a view in the 'home' app)
handler404 = 'home.views.custom_404_view'
urlpatterns = []
    path("", include("yourapp.urls")),  # your app routes
    ]

    if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        
urlpatterns = []
    path("", include("yourapp.urls")),  # replace 'yourapp' with your app name
    ]

    if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        urlpatterns = []
            path('', include('restaurant.urls')),   # your app routes
                path('admin/', admin.site.urls),
                ]

                if settings.DEBUG:
                    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
                    