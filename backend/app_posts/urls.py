from django.urls import path
from .views import PostsListViewSet
from rest_framework import routers


app_name = 'app_posts'

router = routers.DefaultRouter()


router.register('posts', PostsListViewSet, basename='posts')


urlpatterns = router.urls
