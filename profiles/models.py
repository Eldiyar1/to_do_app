from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    username = models.CharField(max_length=150, null=True)
    photo = models.ImageField(upload_to="profile_photos", blank=True, null=True)
    email = models.EmailField(max_length=25, blank=True)
    phone_number = PhoneNumberField(blank=True, null=True)

    def __str__(self):
        return self.username or ''


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title

    def get_author_username(self):
        return [self.author.username]

class Tag(models.Model):
    name = models.CharField(max_length=100)
    posts = models.ManyToManyField(Post, related_name='tags')

    def __str__(self):
        return self.name

    def get_post_tag_names(self):
        return [tag.title for tag in self.posts.all()]


