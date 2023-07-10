from django.contrib import admin
from .models import UserProfile, Post, Tag

admin.site.register(UserProfile)
admin.site.register(Post)
admin.site.register(Tag)