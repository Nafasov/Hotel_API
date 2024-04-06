from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenObtainPairView,
    TokenVerifyView,
    TokenBlacklistView,
    )

from .views import (
    MyProfileAPIView,
    UserRegistrationAPIView,
    )


app_name = 'account'


urlpatterns = [
    path('api/user/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/user/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/user/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/user/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('api/user/register/', UserRegistrationAPIView.as_view(), name='register'),

    path('api/user/profile/', MyProfileAPIView.as_view(), name='profile'),
]