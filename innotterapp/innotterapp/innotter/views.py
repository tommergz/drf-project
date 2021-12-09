from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from innotter.models import User, Tag, Page, Post
from rest_framework import mixins, serializers, viewsets, permissions, generics
from innotter.serializers import UserSerializer, TagSerializer, PageSerializer, PostSerializer
from innotter.service import login


class RegisterViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin
):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(    
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):                                       
    queryset = User.objects.all()

    serializer_classes = {
        "list": UserSerializer,
        "retrieve": UserSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action)

   
    @action(detail=False, methods=['post'], url_path="login")
    def login_user(self, request):
        return login(self, request)


class TagViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
):
    queryset = Tag.objects.all()
    permission_classes = (
        permissions.IsAuthenticated,
    )
    serializer_classes = {
        "list": TagSerializer,
    }
    
    def get_serializer_class(self):
        return self.serializer_classes.get(self.action)


class PageViewSet(
  viewsets.GenericViewSet,
  mixins.RetrieveModelMixin,
  mixins.CreateModelMixin
):
    queryset = Page.objects.all()

    permission_classes = (
        permissions.IsAuthenticated,
    )

    serializer_classes = {
        "retrieve": PageSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action)


class PostViewSet(
  viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):
    queryset = Post.objects.all()

    permission_classes = (
        permissions.IsAuthenticated,
    )

    serializer_classes = {
        "list": PostSerializer,
        "retrieve": PostSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action)
