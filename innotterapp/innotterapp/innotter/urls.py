from rest_framework import routers
from django.urls import path, include
from innotter.views import UserViewSet, TagViewSet, PageDetailViewSet, PostViewSet
router = routers.DefaultRouter()
router.register('api/users', UserViewSet, 'users')
router.register('api/tags', TagViewSet, 'tags')
router.register('api/page', PageDetailViewSet, 'page')
router.register('api/post', PostViewSet, 'post')


urlpatterns = [
  path('', include(router.urls))
]
