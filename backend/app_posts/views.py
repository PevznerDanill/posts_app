from django.shortcuts import render
from .models import Post, Comment
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView, CreateAPIView
from rest_framework.mixins import DestroyModelMixin
from .serializers import PostListSerializer, PostSerializer, CommentSerializer
from .permissions import IsAdminOrReadOnly
from rest_framework import permissions
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .filters import PostFilter


class PostListCreateAPIView(ListCreateAPIView):
    """
    An API View to display the list of Post instances and.
    """
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = PostFilter
    ordering_fields = ['created_at', 'title']


class PostDetailAPIView(RetrieveDestroyAPIView):
    queryset = Post.objects.prefetch_related('comments').all()
    serializer_class = PostSerializer
    permission_classes = [IsAdminOrReadOnly]


class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)







