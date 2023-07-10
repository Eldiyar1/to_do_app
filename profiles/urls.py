from django.urls import path
from .views import UserListAPIView, UserDetailAPIView, PostListAPIView, PostDetailAPIView, \
    TagListAPIView, TagDetailAPIView

urlpatterns = [
    path('users/', UserListAPIView.as_view()),
    path('users/<int:pk>/', UserDetailAPIView.as_view()),
    path('posts/', PostListAPIView.as_view()),
    path('posts/<int:pk>/', PostDetailAPIView.as_view()),
    path('tags/', TagListAPIView.as_view()),
    path('tags/<int:pk>/', TagDetailAPIView.as_view()),
]