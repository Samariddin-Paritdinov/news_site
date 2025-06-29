from rest_framework import generics
from news.models import News
from news.api_endpoints.News.NewsList.serializers import NewsListSerializer


class NewsListAPIView(generics.ListAPIView):
    queryset = News.objects.filter(is_active=True)
    serializer_class = NewsListSerializer
    permission_classes = []

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_authenticated:
            qs = qs.filter(required_login=False)
        return qs