from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.permissions import AllowAny # Allow unauthenticated access for registration
from rest_framework.response import Response
from rest_framework.serializers import Serializer, CharField # Import necessary serializer fields

class UserRegistrationSerializer(Serializer):
    """
    Serializer for user registration.
    Handles validation for username, email, and password.
    """
    username = CharField(max_length=150)
    email = CharField(max_length=255)
    password = CharField(write_only=True) # password should not be readable after creation

    def validate_email(self, value):
        """
        Validate that the email is unique.
        """
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email address is already in use.")
        return value

    def validate_username(self, value):
        """
        Validate that the username is unique.
        """
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("This username is already taken.")
        return value

    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        """
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class UserRegistrationView(generics.CreateAPIView):
    """
    API view for user registration.
    - POST: Registers a new user.
    Allows any user (even unauthenticated) to access this endpoint.
    """
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny] # Allow unauthenticated users to register

    def create(self, request, *args, **kwargs):
        """
        Override the create method to provide a custom success response.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save() # Saves the user

        # Customize the response data for successful registration
        response_data = {
            "message": "User registered successfully",
            "user_id": user.id,
            "username": user.username,
            "email": user.email,
        }
        return Response(response_data, status=status.HTTP_201_CREATED)

