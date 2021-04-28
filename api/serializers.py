from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    This class serialize the User model for API.
    """
    class Meta:
        model = User
        fields = "__all__"
