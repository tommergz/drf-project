from rest_framework import routers
from .api import UserViewSet, TagViewSet, PageDetailViewSet


router = routers.DefaultRouter()
router.register('api/users', UserViewSet, 'users')
router.register('api/tags', TagViewSet, 'tags')
router.register('api/page', PageDetailViewSet, 'page')


urlpatterns = router.urls
