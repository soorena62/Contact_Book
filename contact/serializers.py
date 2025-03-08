from rest_framework import serializers
from .models import Contact, CustomUser
# Create Your serializers Here:


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', "username", "password", "email"]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            email=validated_data["email"]
        )
        return user


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ("id", "first_name", "last_name", "user", "phone_number", "email", "created_at", "updated_at")
        read_only_fields = ('id', 'user', 'created_at', 'updated_at')
