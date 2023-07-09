from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('photo', 'email', 'phone_number')


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(read_only=True)  # read_only=True для связанного поля

    class Meta:
        model = User
        fields = ('id', 'profile')