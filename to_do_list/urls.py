from django.urls import path
from .views import TaskListAPIView, TaskDetailAPIView

urlpatterns = [
    path('tasks/', TaskListAPIView.as_view()),
    path('tasks/<int:id>/', TaskDetailAPIView.as_view())
]
from rest_framework.generics import ListAPIView