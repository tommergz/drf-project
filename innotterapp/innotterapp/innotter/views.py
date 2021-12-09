from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.contrib import auth
from rest_framework.decorators import action
import jwt, datetime

from innotter.models import User, Tag, Page, Post
from rest_framework import mixins, serializers, viewsets, permissions, generics
from innotter.serializers import UserSerializer, TagSerializer, PageDetailSerializer, PostSerializer


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
        data = request.data
        username = data.get('username', '')
        password = data.get('password', '')
        user = auth.authenticate(username=username, password=password)

        if user:
            payload = {
                'id': user.id,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
                'iat': datetime.datetime.utcnow()
            }
            auth_token = jwt.encode(
                payload, settings.JWT_SECRET_KEY, algorithm="HS256")

            serializer = UserSerializer(user)

            data = {'user': serializer.data, 'token': auth_token}

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


class PageDetailViewSet(
  viewsets.GenericViewSet,
  mixins.RetrieveModelMixin
):
    queryset = Page.objects.all()

    permission_classes = (
        permissions.IsAuthenticated,
    )

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

    permission_classes = (
        permissions.IsAuthenticated,
    )

    serializer_classes = {
        "list": PostSerializer,
        "retrieve": PostSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action)
