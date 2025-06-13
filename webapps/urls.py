from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView, # View to obtain a new access and refresh token
    TokenRefreshView,    # View to refresh an access token
)

urlpatterns = [
    # Django Admin Panel URL
    path('admin/', admin.site.urls),

    # API authentication endpoints from djangorestframework-simplejwt
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Include URLs from our 'users' app (for registration)
    # This will typically expose /api/register/
    path('api/', include('users.urls')),

    # Include URLs from our 'customers' app (for CRUD operations)
    # This will typically expose /api/customers/ and /api/customers/<id>/
    path('api/', include('customers.urls')),
]
