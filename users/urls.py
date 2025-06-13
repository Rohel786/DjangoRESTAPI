from django.urls import path
from .views import UserRegistrationView

urlpatterns = [
    # URL for user registration
    path('register/', UserRegistrationView.as_view(), name='register'),
]
