from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import Http404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Gift
from .tasks import pick_winner, print_expiration
from .serializers import GetGiftSerializer, AddGiftSerializer
from datetime import datetime, timedelta
from django.utils import timezone
from rest_framework.parsers import MultiPartParser, FormParser
from django.contrib.auth import get_user_model
User = get_user_model()

class GiftList(APIView):

    # parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        gifts = Gift.objects.filter(giver__city=request.user.city, giver__state=request.user.state)
        serializer = GetGiftSerializer(gifts, many=True)
        return Response(serializer.data)

    def post(self, request):
        request.data.__setitem__('giver', request.user.id)
        request.data.__setitem__('active', True)
        serializer = AddGiftSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            expiration = timezone.now() + timedelta(hours=serializer.data['hours_active'])
            # celery task
            pick_winner.apply_async([serializer.data['id']], eta=expiration)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', serializer.errors, serializer.data)
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
        serializer = GetGiftSerializer(gift)
        return Response(serializer.data)

    def put(self, request, pk):
        gift = self.get_object(pk)
        if gift.giver.id == request.user.id:
            serializer = AddGiftSerializer(gift, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def patch(self, request, pk):
        gift = self.get_object(pk)
        serializer = AddGiftSerializer(gift, data=request.data, partial=True)
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