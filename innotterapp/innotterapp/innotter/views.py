from django.shortcuts import render
from rest_framework.response import Response

from innotter.models import User, Tag, Page, Post
from rest_framework import mixins, viewsets, permissions
from innotter.serializers import UserSerializer, TagSerializer, PageDetailSerializer, PostSerializer


class UserViewSet(    
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
  ):
    queryset = User.objects.all()
    permission_classes = (
        permissions.AllowAny,
    )
    serializer_classes = {
        "list": UserSerializer,
        "retrieve": UserSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action)


class TagViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
  ):
    queryset = Tag.objects.all()
    permission_classes = (
        permissions.AllowAny,
    )
    serializer_classes = {
        "list": TagSerializer,
    }
    
    def get_serializer_class(self):
        return self.serializer_classes.get(self.action)


class PageDetailViewSet(
  viewsets.GenericViewSet,
  mixins.RetrieveModelMixin
):
    queryset = Page.objects.all()

    serializer_classes = {
        "retrieve": PageDetailSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action)


class PostViewSet(
  viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):
    queryset = Post.objects.all()

    serializer_classes = {
        "list": PostSerializer,
        "retrieve": PostSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action)
