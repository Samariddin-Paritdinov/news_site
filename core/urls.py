from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


schema_view = get_schema_view(
   openapi.Info(
      title="eCommerce API",
      default_version='v1',
      description="eCommerce platform API documentation",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="admin@@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
   authentication_classes=[],
)


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path("profile/", include("accounts.api_endpoints.Profile.urls"), name="profile"),
    path("media-file/", include("common.api_endpoints.MediaFile.urls"), name="media"),

    path("tag-category/", include("news.api_endpoints.TagCategory.urls"), name="tag-category"),
    path("news/", include("news.api_endpoints.News.urls"), name="news"),



    path('admin/', admin.site.urls),
    # Swagger and Redoc URLs
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('i18n/', include('django.conf.urls.i18n')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls'))
    ]
