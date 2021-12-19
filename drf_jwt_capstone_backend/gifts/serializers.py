from rest_framework import serializers
from .models import Gift

class GiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gift
        fields = ['id', 'giver', 'winner',  'name', 'description', 'category', 'condition', 'active', 'interested_users', 'created', 'expiration']