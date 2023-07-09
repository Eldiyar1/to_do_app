from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    photo = models.ImageField(upload_to="profile_photos", blank=True, null=True)
    email = models.EmailField(max_length=25, blank=True)
    phone_number = PhoneNumberField(blank=True, null=True)

    def __str__(self):
        return self.user.username


