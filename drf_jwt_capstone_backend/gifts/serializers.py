from rest_framework import serializers
from .models import Gift

class GiftSerializer(serializers.ModelSerializer):
    giver = serializers.SlugRelatedField(read_only=True, slug_field='username')
    class Meta:
        model = Gift
        fields = ['id', 'giver', 'winner',  'name', 'description', 'category', 'condition', 'active', 'interested_users', 'created', 'image', 'hours_active']