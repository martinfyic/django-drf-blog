from django.contrib import admin
from django.urls import path, include
# from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Django REST framework BLOG",
        default_version='v1',
        description="Api para blog",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="martin.f.yic@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    #    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('api.urls')),
    path('user/', include('user.urls')),

    # Documentation Path
    path('doc', schema_view.with_ui(
        'swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
]
