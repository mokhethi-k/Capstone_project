from django.shortcuts import render
from .serializers import UserSerializer, ProfileSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets, mixins
from .permissions import UserPermisions, IsProfileOwnweOrReadOnly, IsSuperUserOrReadOnly
from .models import Profile
from rest_framework.permissions import IsAuthenticated



class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [UserPermisions, IsAuthenticated]
    queryset = User.objects.all()
    serializer_class  = UserSerializer


class ProfileViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    queryset = Profile.objects.all()
    permission_classes = [IsProfileOwnweOrReadOnly, IsSuperUserOrReadOnly]
    serializer_class = ProfileSerializer




