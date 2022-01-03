from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import Http404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Gift
from .tasks import pick_winner, print_expiration
from .serializers import GiftSerializer
from datetime import datetime, timedelta
from django.utils import timezone
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
            print(serializer.data['expiration'])
            # expiration = timezone.now() + timedelta(hours=1)
            # celery task
            pick_winner.apply_async([serializer.data['id']], eta=serializer.data['expiration'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GiftDetail(APIView):

    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Gift.objects.get(pk=pk)
        except Gift.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        gift = self.get_object(pk)
        serializer = GiftSerializer(gift)
        return Response(serializer.data)

    def put(self, request, pk):
        gift = self.get_object(pk)
        if gift.giver.id == request.user.id:
            serializer = GiftSerializer(gift, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def patch(self, request, pk):
        gift = self.get_object(pk)
        serializer = GiftSerializer(gift, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        gift = self.get_object(pk)
        if gift.giver.id == request.user.id:
            gift.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_401_UNAUTHORIZED)