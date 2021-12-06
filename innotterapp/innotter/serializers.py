from rest_framework import serializers
from .models import User, Tag, Page


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class PageDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = '__all__'
