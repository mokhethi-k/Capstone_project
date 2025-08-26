from django.shortcuts import render
from .serializers import UserSerializer, ProfileSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets
from .permissions import UserPermisions
from .models import Profile


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [UserPermisions,]
    queryset = User.objects.all()
    serializer_class  = UserSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

