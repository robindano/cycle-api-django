from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from .serializers import RegistrationSerializer, UserSerializer, ChangePasswordSerializer, UpdateUserSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

class ChangePassword(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer

class UpdateProfile(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateUserSerializer

class GetUser(APIView):

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

