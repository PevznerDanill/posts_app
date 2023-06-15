from django_filters import rest_framework as filters
from .models import Post


class PostFilter(filters.FilterSet):
    """
        A filter for the PostListAPIView (model Animal).
        Allows to filter the list by the post's title and time of creation.
    """

    class Meta:
        model = Post
        fields = 'title', 'created_at',

