from rest_framework import serializers
from news.models import News


class NewsCreateSerializer(serializers.ModelSerializer):
    """
    Создание новости: slug, счётчики и даты — недоступны.
    """
    required_login = serializers.BooleanField()

    class Meta:
        model = News
        fields = [
            'title',
            'content',
            'categories',
            'tags',
            'is_active',
            'required_login',
            'author',
            'default_image',
            'media',
        ]