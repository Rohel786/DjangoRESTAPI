from rest_framework import serializers
from .models import Customer
import re # Import regex for mobile validation

class CustomerSerializer(serializers.ModelSerializer):
    """
    Serializer for the Customer model.
    Handles serialization/deserialization and validation of Customer data.
    """
    class Meta:
        model = Customer
        # Define the fields to be included in the serialized output.
        # 'read_only_fields' are included in output but cannot be set by client.
        fields = ['id', 'name', 'email', 'mobile', 'address', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate_email(self, value):
        """
        Custom validation for the email field.
        Ensures the email is unique (beyond the model's unique=True constraint,
        this handles race conditions or provides a more specific error message
        during creation/update in the serializer context).
        """
        # Get the current instance if it's an update operation
        instance = self.instance

        # Check if an instance exists (i.e., this is an update operation)
        if instance and instance.email == value:
            # If the email hasn't changed, no need to validate uniqueness against others
            return value

        # Check if email already exists in the database
        if Customer.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email address is already in use.")
        return value

    def validate_mobile(self, value):
        """
        Custom validation for the mobile field.
        Ensures the mobile number is in a valid format (e.g., starts with +,
        followed by digits, or just digits).
        """
        # Example: Basic validation for mobile format (e.g., "+1234567890" or "9876543210")
        # Adjust regex as per your specific mobile number format requirements.
        if not re.fullmatch(r'^\+?[0-9]{7,15}$', value):
            raise serializers.ValidationError(
                "Mobile number must be in a valid format (e.g., +1234567890 or 9876543210)."
            )
        return value

