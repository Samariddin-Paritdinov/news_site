from rest_framework import serializers
from news.models import News
from common.models import MediaFile
from django.contrib.auth import get_user_model

User = get_user_model()


class NewsRetrieveSerializer(serializers.ModelSerializer):
    """
    Детальный просмотр одной новости: все поля.
    """
    author     = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    media      = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=MediaFile.objects.all(),
        required=False,
        allow_null=True
    )

    class Meta:
        model = News
        fields = [
            'id',
            'title',
            'slug',
            'content',
            'categories',
            'tags',
            'is_active',
            'required_login',
            'author',
            'default_image',
            'media',
            'like_count',
            'created_at',
            'updated_at',
        ]
        read_only_fields = [
            'id',
            'slug',
            'like_count',
            'created_at',
            'updated_at',
        ]