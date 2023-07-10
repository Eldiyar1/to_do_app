from .models import Task, Category, Tag
from .serializers import TaskSerializer, CategorySerializer, TagSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.pagination import PageNumberPagination


class Paginator(PageNumberPagination):
    page_size = 2

class TaskListAPIView(ListCreateAPIView):
    serializer_class = TaskSerializer
    pagination_class = Paginator

    def get_queryset(self):
        queryset = Task.objects.all()
        completed = self.kwargs.get('completed')

        if completed:
            queryset = queryset.filter(completed=completed)

        return queryset


class TaskDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'id'


class TaskSearchAPIView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        query = self.kwargs.get('q')

        if query:
            queryset = Task.objects.filter(title__icontains=query)
        else:
            queryset = Task.objects.all()

        return queryset

class CategoryListAPIView(ListCreateAPIView):
    queryset = Category
    serializer_class = CategorySerializer
    pagination_class = Paginator


class CategoryDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category
    serializer_class = CategorySerializer

class TagListAPIView(ListCreateAPIView):
    queryset = Tag
    serializer_class = TagSerializer
    pagination_class = Paginator


class TagDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Tag
    serializer_class = TagSerializer


# @api_view(['GET', 'POST'])
# def task_list_api_view(request):
#     if request.method == 'GET':
#         queryset = Task.objects.all()
#         completed = request.GET.get('completed')
#
#         if completed:
#             queryset = queryset.filter(completed=completed)
#         serializer = TaskSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = TaskSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def task_detail_api_view(request, id):
#     try:
#         task = Task.objects.get(id=id)
#     except Task.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = TaskSerializer(task)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = TaskSerializer(task, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         task.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(['GET'])
# def task_search_api_view(request, q):
#     if q:
#         queryset = Task.objects.filter(title__icontains=q)
#     else:
#         queryset = Task.objects.all()
#
#     serializer = TaskSerializer(queryset, many=True)
#     return Response(serializer.data)



