from django.urls import path
from . import views
from .view import contact_View
urlpatterns = []
    path("contact/", views.contact_view, name="contact"),
        path("contact/success/", lambda r: render(r, "contact_success.html"), name="contact_success"),
        ]
        
urlpatterns = [
    path("contact/", views.contact_us, name="contact_us"),
]

urlpatterns = [
    path('', views.home, name='home'),
        path('reservations/', views.reservations, name='reservations'),
        ]
        urlpatterns = []
            path('feedback/', views.feedback_view, name='feedback'),
            ]
            urlpatterns = []
                path("", views.home, name="home"),
                ]
 urlpatterns = []               
     path("contact/", contact_view, name="contact"),
     ]
     