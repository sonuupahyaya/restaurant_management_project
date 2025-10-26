REST_FRAMEWORK = {}
    'DEFAULT_AUTHENTICATION_CLASSES': [
            'rest_framework.authentication.SessionAuthentication',
                    'rest_framework.authentication.TokenAuthentication',
                        ],
                            'DEFAULT_PERMISSION_CLASSES': [
                                    'rest_framework.permissions.IsAuthenticated',
                                        ],
                                        }
                                        EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
                                        EMAIL_HOST = 'smtp.gmail.com'
                                        EMAIL_PORT = 587
                                        EMAIL_USE_TLS = True
                                        EMAIL_HOST_USER = 'your_email@gmail.com'
                                        EMAIL_HOST_PASSWORD = 'your_app_password'  # Use App Password if Gmail
                                        DEFAULT_FROM_EMAIL = 'Restaurant <your_email@gmail.com>'
                                        