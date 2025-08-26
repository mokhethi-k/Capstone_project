from django.shortcuts import render
from .serializers import UserSerializer, ProfileSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets, mixins
from .permissions import UserPermisions, IsProfileOwnweOrReadOnly
from .models import Profile


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [UserPermisions,]
    queryset = User.objects.all()
    serializer_class  = UserSerializer


class ProfileViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    permission_classes = [IsProfileOwnweOrReadOnly,]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

