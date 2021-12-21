from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, ChangePassword, UpdateProfile, GetUser

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('change_password/<int:pk>/', ChangePassword.as_view(), name='auth_change_password'),
    path('update_profile/<int:pk>/', UpdateProfile.as_view(), name='auth_update_profile'),
    path('user/', GetUser.as_view(), name='get_user')
]
