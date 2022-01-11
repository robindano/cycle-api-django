from rest_framework import serializers
from authentication.serializers import UserSerializer
from .models import Comment

class GetCommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ['id', 'author', 'gift',  'content', 'created_at', 'parent']

class AddCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author', 'gift',  'content', 'created_at', 'parent']