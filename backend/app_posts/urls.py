from django.urls import path
from .views import PostListCreateAPIView, PostDetailAPIView, CommentCreateAPIView

app_name = 'app_posts'

urlpatterns = [
    path('posts/', PostListCreateAPIView.as_view(), name='posts'),
    path('posts/<int:pk>/', PostDetailAPIView.as_view(), name='post_detail'),
    path('comment/', CommentCreateAPIView.as_view(), name='comment')
]
