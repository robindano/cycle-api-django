from rest_framework import serializers

from authentication.serializers import UserSerializer
from .models import Gift

class GetGiftSerializer(serializers.ModelSerializer):
    giver = UserSerializer(read_only=True)
    winner = UserSerializer(allow_null=True)
    class Meta:
        model = Gift
        fields = ['id', 'giver', 'winner',  'name', 'description', 'category', 'condition', 'active', 'interested_users', 'created', 'image', 'hours_active']

class AddGiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gift
        fields = ['id', 'giver', 'winner',  'name', 'description', 'category', 'condition', 'active', 'interested_users', 'created', 'image', 'hours_active']