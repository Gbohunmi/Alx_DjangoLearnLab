from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

# Create your views here.

class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] #Allows any user to view posts.

    def perform_create(self, serializer):
        # Automatically sets the current user as the author when creating a post.
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]#Allows only authenticated users to view posts.


    def perform_create(self, serializer):
        # Automatically sets the current user as the author when creating a comment.
        serializer.save(author=self.request.user)

