from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True, slug_field='username')
    class Meta:
        model = Comment
        fields = ['id', 'author', 'gift',  'content', 'created_at', 'parent']