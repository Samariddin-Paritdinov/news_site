from rest_framework import serializers
from news.models import News


class NewsListSerializer(serializers.ModelSerializer):
    """
    Список новостей: только краткие поля для списка.
    """

    class Meta:
        model = News
        fields = [
            'id',
            'title',
            'slug',
            'is_active',
            'required_login',
            'like_count',
            'created_at',
            'updated_at',
        ]