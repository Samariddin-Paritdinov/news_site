from django.urls import path
from news.api_endpoints.News import (
    NewsListAPIView,
    NewsUpdateAPIView,
    NewsCreateAPIView,
    NewsDeleteAPIView,
    NewsRetrieveAPIView
)

urlpatterns = [
    path('read/', NewsListAPIView.as_view(), name='news-list'),
    path('create/', NewsCreateAPIView.as_view(), name='news-create'),
    path('read/<int:id>/', NewsRetrieveAPIView.as_view(), name='news-detail'),
    path('update/<int:id>/', NewsUpdateAPIView.as_view(), name='news-update'),
    path('delete/<int:id>/', NewsDeleteAPIView.as_view(), name='news-delete'),
]