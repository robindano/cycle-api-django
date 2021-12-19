from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Gift
from .serializers import GiftSerializer
from django.contrib.auth import get_user_model
User = get_user_model()

class GiftList(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        gifts = Gift.objects.filter(giver__city=request.user.city, giver__state=request.user.state)
        serializer = GiftSerializer(gifts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GiftSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)