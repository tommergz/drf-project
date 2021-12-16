from rest_framework import serializers
from innotter.models import User, Tag, Page, Post

from innotter.s3_service import add_file


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'role',
            'title',
            'is_blocked',
            'password',
        )

    def validate(self, attrs):
        email = attrs.get('email', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email', ('Email is already in use')}
            )
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=65, min_length=8, write_only=True)
    username = serializers.CharField(max_length=255, min_length=2)

    class Meta:
        model = User
        fields = ['username', 'password']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'name',
        )


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = (
            'name',
            'description',
            'uuid',
            'tags',
            'image',
            'owner',
            'followers',
            'is_private',
            'follow_requests'
        )


    def create(self, validated_data):
        image_name = None
        if validated_data.__contains__('image'):
            image_name = add_file(validated_data['image'])
            validated_data['image'] = image_name
        return Page.objects.create(**validated_data)


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'page',
            'content',
            'created_at',
            'updated_at',
        )
        