from rest_framework.response import Response

from .models import User, Tag, Page
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, TagSerializer, PageDetailSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TagSerializer


class PageDetailViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageDetailSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
