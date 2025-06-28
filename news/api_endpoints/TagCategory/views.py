from rest_framework import viewsets
from news.models import Category, Tag
from news.api_endpoints.TagCategory.serializers import CategorySerializer, TagSerializer
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
  def has_permission(self, request, view):
    return bool(
        request.method in SAFE_METHODS or
        (request.user and request.user.is_staff)
    )

class CategoryViewSet(viewsets.ModelViewSet): 
  queryset = Category.objects.all()
  serializer_class = CategorySerializer
  permission_classes = [IsAdminOrReadOnly]
  lookup_field = 'id'


class TagViewSet(viewsets.ModelViewSet):
  queryset = Tag.objects.all()
  serializer_class = TagSerializer
  permission_classes = [IsAdminOrReadOnly]
  lookup_field = 'id'
