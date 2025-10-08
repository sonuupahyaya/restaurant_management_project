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
     urlpatterns = []
         path("", views.home, name="home"),
             path("menu/", views.menu_page, name="menu"),
                 path("about/", views.about_page, name="about"),
                     path("faq/", views.faq_page, name="faq"),  # 👈 New FAQ page
                     ]
                     from django.urls import path
                     from django.contrib.auth import views as auth_views
                     from . import views

                     urlpatterns = [
                         path('', views.home, name='home'),
                             path('login/', auth_views.LoginView.as_view(template_name='restaurant/home.html'), name='login'),
                                 path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
                                 ]
                                 from django.urls import path
                                 from .views import MenuCategoryListView

                                 urlpatterns = [
                                     path('api/menu-categories/', MenuCategoryListView.as_view(), name='menu-categories-list'),
                                     ]
                                     