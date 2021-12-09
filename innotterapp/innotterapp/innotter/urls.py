from rest_framework import routers
from django.urls import path, include
from innotter.views import UserViewSet, TagViewSet, PageDetailViewSet, PostViewSet, RegisterViewSet

router = routers.DefaultRouter()
router.register('api/users', UserViewSet, 'users')
router.register('api/tags', TagViewSet, 'tags')
router.register('api/page', PageDetailViewSet, 'page')
router.register('api/post', PostViewSet, 'post')
router.register('api/register', RegisterViewSet, 'register')


urlpatterns = [
  path('', include(router.urls)),
  # path(r'api/login', LoginView.as_view()),
]
