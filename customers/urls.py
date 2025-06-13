from django.urls import path
from .views import CustomerListCreateAPIView, CustomerRetrieveUpdateDestroyAPIView

urlpatterns = [
    # URL for listing all customers and creating a new customer
    path('customers/', CustomerListCreateAPIView.as_view(), name='customer-list-create'),

    # URL for retrieving, updating, or deleting a specific customer by UUID
    # The <uuid:id> path converter ensures that the ID is a valid UUID.
    path('customers/<uuid:id>/', CustomerRetrieveUpdateDestroyAPIView.as_view(), name='customer-detail'),
]
