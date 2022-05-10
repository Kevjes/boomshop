from rest_framework import routers
from django.urls import path
from users.views import get_user_data, login_api, register_api

router = routers.DefaultRouter()

urlpatterns = [
    path('login/', login_api),
    path('user/', get_user_data),
    path('register/', register_api)
]