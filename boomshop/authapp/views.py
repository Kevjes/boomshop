from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from authapp.serializers import UserSerializer
# Create your views here.

class AllUsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AllSuperUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_superuser=True)
    serializer_class = UserSerializer

class AllCustomerUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_superuser=False)
    serializer_class = UserSerializer