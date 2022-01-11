from decimal import ConversionSyntax
from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import Http404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Comment
from .serializers import GetCommentSerializer, AddCommentSerializer
from django.contrib.auth import get_user_model
User = get_user_model()

class CommentList(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, gift_id):
        comments = Comment.objects.filter(gift__id=gift_id)
        serializer = GetCommentSerializer(comments, many=True)
        return Response(serializer.data) 

    def post(self, request, gift_id):
        serializer = AddCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentDetail(APIView):

    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except:
            raise status.HTTP_404_NOT_FOUND    

    def get(self, request, gift_id, pk):
        comment = self.get_object(pk)
        serializer = GetCommentSerializer(comment)
        return Response(serializer.data)

    def put(self, request, gift_id, pk):
        comment = self.get_object(pk)
        if comment.author.id == request.user.id:
            serializer = AddCommentSerializer(comment, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, gift_id, pk):
        comment = self.get_object(pk)
        print(comment.author)
        print(request.user)
        if comment.author == request.user:
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
