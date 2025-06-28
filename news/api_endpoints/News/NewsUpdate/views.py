from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.exceptions import PermissionDenied
from news.models import News
from news.api_endpoints.News.NewsUpdate.serializers import NewsUpdateSerializer

class NewsUpdateAPIView(generics.UpdateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsUpdateSerializer
    lookup_field = 'id'
    permission_classes = [IsAdminUser]