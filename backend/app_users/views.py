from django.shortcuts import render
from rest_framework import mixins, viewsets
from .serializers import SpecialUserSerializer
from django.contrib.auth.models import User


class SpecialUserViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
