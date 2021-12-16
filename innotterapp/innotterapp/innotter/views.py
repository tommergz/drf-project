from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
import jwt, datetime
from django.contrib import auth
from rest_framework.decorators import action

from django.conf import settings
from innotter.models import User, Tag, Page, Post
from rest_framework import mixins, serializers, viewsets, permissions, generics
from innotter.serializers import UserSerializer, TagSerializer, PageSerializer, PostSerializer
from innotter.service import login_user, get_new_follower_id


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
    def login(self, request):
        data = login_user(request)

        if data:
            return Response(data, status=status.HTTP_200_OK)
    
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


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
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    queryset = Page.objects.all()

    permission_classes = (
        permissions.IsAuthenticated,
    )

    serializer_classes = {
        "create": PageSerializer,
        "list": PageSerializer,
        "retrieve": PageSerializer,
        "partial_update": PageSerializer
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action)

    @action(detail=True, methods=['post'], url_path="add_follower")
    def add_follower(self, request, pk):
        id = get_new_follower_id(self, request)
    
        return Response(id, status=status.HTTP_200_OK)


class PostViewSet(
  viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):
    queryset = Post.objects.all()

    permission_classes = (
        permissions.IsAuthenticated,
    )

    serializer_classes = {
        "create": PostSerializer,
        "list": PostSerializer,
        "retrieve": PostSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action)
