from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.exceptions import PermissionDenied
from news.models import News
from news.api_endpoints.News.NewsCreate.serializers import NewsCreateSerializer


class NewsCreateAPIView(generics.CreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsCreateSerializer
    permission_classes = [IsAdminUser]