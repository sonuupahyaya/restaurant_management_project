from django.apps import AppConfig

class AccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
        name = 'account'
        class RestaurantConfig(AppConfig):
                default_auto_field = 'django.db.models.BigAutoField'
                    name = 'restaurant'  # change to your app name

                        def ready(self):
                                import restaurant.signals  # import signals
                                