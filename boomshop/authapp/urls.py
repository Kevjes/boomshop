from rest_framework import routers

from authapp.views import *

router = routers.DefaultRouter()
router.register('all-users', AllUsersViewSet)
router.register('all-super-users', AllSuperUserViewSet)
router.register('all-customer', AllCustomerUserViewSet)
