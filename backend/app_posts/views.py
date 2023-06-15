from .models import Post, Comment
from .serializers import PostListSerializer, PostSerializer, CommentSerializer
from .permissions import IsAdminOrReadOnly
from rest_framework.response import Response
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .filters import PostFilter
from rest_framework import mixins, viewsets


class PostsListViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    View set to return a list of posts and create one.
    """
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = PostFilter
    ordering_fields = ['created_at', 'title']

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = PostSerializer(instance)
        return Response(serializer.data)






