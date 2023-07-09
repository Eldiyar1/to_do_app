from django.urls import path
from .views import TaskListAPIView, TaskDetailAPIView, TaskSearchAPIView

urlpatterns = [
    path('tasks/', TaskListAPIView.as_view()),
    path('tasks/<int:id>/', TaskDetailAPIView.as_view()),
    path('tasks/completed/', TaskListAPIView.as_view()),
    path('tasks/search/<str:q>/', TaskSearchAPIView.as_view())
]

# urlpatterns = [
#     path('tasks/', task_list_api_view),
#     path('tasks/completed/', task_list_api_view),
#     path('tasks/<int:id>/', task_detail_api_view),
#     path('tasks/search/<str:q>/', task_search_api_view),
# ]
