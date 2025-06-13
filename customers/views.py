from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from webapps.pagination import StandardResultsPagination
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Customer
from .serializers import CustomerSerializer

class CustomerListCreateAPIView(generics.ListCreateAPIView):
    """
    API view to list all customers and create a new customer.
    - GET: Lists all customers with pagination and search functionality.
    - POST: Creates a new customer.
    Requires JWT authentication.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated] # Ensures only authenticated users can access
    pagination_class = StandardResultsPagination # Apply custom pagination
    filter_backends = [DjangoFilterBackend, SearchFilter] # Enable filtering and searching

    # Search by 'name' or 'email' fields
    search_fields = ['name', 'email']

    def perform_create(self, serializer):
        """
        Override perform_create to handle object creation.
        Could add additional logic here, e.g., logging or user association.
        """
        serializer.save()

    def post(self, request, *args, **kwargs):
        """
        Handle POST request to create a new customer.
        Returns 201 Created on success, 400 Bad Request on validation errors.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True) # Raise 400 if validation fails
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CustomerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a specific customer.
    - GET: Retrieves a customer by ID.
    - PUT: Updates a customer by ID (full update).
    - PATCH: Partially updates a customer by ID.
    - DELETE: Deletes a customer by ID.
    Requires JWT authentication.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated] # Ensures only authenticated users can access
    lookup_field = 'id' # Specifies that the URL lookup will be by the 'id' field (UUID)

    def put(self, request, *args, **kwargs):
        """
        Handle PUT request for full update of a customer.
        Returns 200 OK on success, 400 Bad Request on validation errors,
        404 Not Found if customer does not exist.
        """
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        """
        Handle PATCH request for partial update of a customer.
        Returns 200 OK on success, 400 Bad Request on validation errors,
        404 Not Found if customer does not exist.
        """
        # partial=True allows partial updates (not all fields are required)
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        Handle DELETE request to delete a customer.
        Returns 204 No Content on success, 404 Not Found if customer does not exist.
        """
        instance = self.get_object() # Get the customer instance
        self.perform_destroy(instance) # Perform the deletion
        return Response(status=status.HTTP_204_NO_CONTENT)

