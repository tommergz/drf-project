from rest_framework import routers
from django.urls import path, include
from innotter.views import UserViewSet, TagViewSet, PageViewSet, PostViewSet, RegisterViewSet

router = routers.DefaultRouter()
router.register('api/users', UserViewSet, 'users')
router.register('api/tags', TagViewSet, 'tags')
router.register('api/page', PageViewSet, 'page')
router.register('api/post', PostViewSet, 'post')
router.register('api/register', RegisterViewSet, 'register')


urlpatterns = [
  path('', include(router.urls)),
]
