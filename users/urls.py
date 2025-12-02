from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserRegisterView, UserViewSet

router = DefaultRouter()
router.register(r'', UserViewSet, basename='user')

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('', include(router.urls)),
]
