from django.urls import path
from .views import SpecialUserViewSet
from rest_framework import routers


app_name = 'app_users'

router = routers.DefaultRouter()


router.register('', SpecialUserViewSet, basename='users')


urlpatterns = router.urls
