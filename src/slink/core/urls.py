from rest_framework.routers import DefaultRouter

from slink.core.views import LinkGenericViewSet


router = DefaultRouter()
router.register(r'', LinkGenericViewSet, basename='link')

urlpatterns = router.urls
