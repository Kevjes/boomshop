# from django.shortcuts import render
# from rest_framework import viewsets
# from django.contrib.auth.models import User
# from users.serializers import UserSerializer
# # Create your views here.

# class AllUsersViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class AllSuperUserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.filter(is_superuser=True)
#     serializer_class = UserSerializer

# class AllCustomerUserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.filter(is_superuser=False)
#     serializer_class = UserSerializer

from venv import create
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken

from users.serializers import RegisterSerialize

@api_view(['POST'])
def login_api(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']

    _, token = AuthToken.objects.create(user)

    return Response({
        'user':{
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'is_staff': user.is_staff,
        },
        'token': token
    })

@api_view(['GET'])
def get_user_data(request):
    user = request.user
    if user.is_authenticated:
        return Response({
            'user':{
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'is_staff': user.is_staff,
            }
        })

    return Response({'error': 'User is not authenticated'})

@api_view(['POST'])
def register_api(request):
    serializer = RegisterSerialize(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = serializer.save()
    _, token = AuthToken.objects.create(user)

    return Response({
        'user':{
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'is_staff': user.is_staff,
        },
        'token': token
    })