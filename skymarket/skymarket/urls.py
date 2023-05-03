from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from djoser.views import UserViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers
from rest_framework_simplejwt import views

from ads.views import AdViewSet, CommentViewSet


router = SimpleRouter()
router.register('api/ads', AdViewSet)
router.register("api/users", UserViewSet, basename="users")

comment_router = routers.NestedSimpleRouter(router, "api/ads", lookup='ads')
comment_router.register("comments", CommentViewSet, basename="comments")

urlpatterns = [
    path("api/admin/", admin.site.urls),
    path("api/redoc-tasks/", include("redoc.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name='schema'),
    path("api/schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # path("api/users/", include('djoser.urls.jwt')),
    path("api/token/", views.TokenObtainPairView.as_view(), name="jwt-create"),
    path("api/token-refresh/", views.TokenRefreshView.as_view(), name="jwt-refresh"),
]
urlpatterns += router.urls
urlpatterns += comment_router.urls

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)