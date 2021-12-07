from rest_framework import serializers
from innotter.models import User, Tag, Page


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email',
            'role',
            'title',
            'is_blocked'
        )


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'name',
        )


class PageDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = (
            'name',
            'description',
            'tags',
            'owner',
            'followers',
            'is_private',
            'follow_requests'
        )
