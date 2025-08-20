from django.shortcuts import render
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets
from .permissions import UserPermisions

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [UserPermisions,]
    queryset = User.objects.all()
    serializer_class  = UserSerializer

