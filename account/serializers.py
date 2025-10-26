from django.contrib.auth.models import User
from rest_framework import serializers

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
            model = User
                    fields = ['first_name', 'last_name', 'email']  # updatable fields only
                            extra_kwargs = {
                                        'email': {'required': False},
                                                    'first_name': {'required': False},
                                                                'last_name': {'required': False},
                                                                        }
                                                                        