from rest_framework.authtoken.admin import User
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import RetrieveAPIView, ListAPIView
from .serializers import UserSerializer
from rest_framework.pagination import PageNumberPagination

class Paginator(PageNumberPagination):
    page_size = '2'


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    pagination_class = Paginator


class UserDetailAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

