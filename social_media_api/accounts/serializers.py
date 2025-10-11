from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    """Serializer for user display and profile."""
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture']


class RegisterSerializer(serializers.ModelSerializer):
    """Serializer for user registration and token creation."""
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        # Create user using Django's built-in create_user method
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        # Create an auth token for the new user
        Token.objects.create(user=user)
        return user
