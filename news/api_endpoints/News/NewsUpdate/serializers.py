from rest_framework import serializers
from news.models import News

class NewsUpdateSerializer(serializers.ModelSerializer):
    """
    Обновление новости: те же поля, что и при создании.
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
            'default_image',
            'media',
        ]