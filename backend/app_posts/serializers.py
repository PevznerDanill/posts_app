from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth.models import User
from app_users.serializers import SpecialUserSerializer


class PostListSerializer(serializers.ModelSerializer):
    """
    A serializer for the representation of an object in a list of Post instances.
    Used in .
    """

    class Meta:
        model = Post
        fields = 'id', 'created_at', 'title', 'description',


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = 'id', 'author', 'created_at', 'content', 'post'

    author = SpecialUserSerializer(read_only=True)


class PostSerializer(serializers.ModelSerializer):
    """
    A serializer for the representation of an object in a list of Post instances.
    Used in .
    """

    class Meta:
        model = Post
        fields = 'id', 'created_at', 'title', 'description', 'content', 'comments'

    comments = CommentSerializer(many=True)

