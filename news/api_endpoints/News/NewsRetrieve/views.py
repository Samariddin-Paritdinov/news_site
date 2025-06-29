from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.exceptions import PermissionDenied
from news.models import News
from news.api_endpoints.News.NewsRetrieve.serializers import NewsRetrieveSerializer

class NewsRetrieveAPIView(generics.RetrieveAPIView):
    queryset = News.objects.filter(is_active=True)
    serializer_class = NewsRetrieveSerializer
    lookup_field = 'id'
    permission_classes = []

    def retrieve(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.required_login and not request.user.is_authenticated:
            raise PermissionDenied("This news requires login to view.")
        return super().retrieve(request, *args, **kwargs)