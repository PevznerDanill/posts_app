from rest_framework import serializers
from django.contrib.auth.models import User
from djoser.serializers import UserSerializer


class SpecialUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = 'id', 'email', 'username', 'is_superuser',
        read_only_fields = 'id', 'is_superuser',
