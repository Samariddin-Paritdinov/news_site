from rest_framework.routers import DefaultRouter
from news.api_endpoints.TagCategory.views import CategoryViewSet, TagViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'tags', TagViewSet)

urlpatterns = router.urls