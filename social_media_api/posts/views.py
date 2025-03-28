from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10  # Default posts per page
    page_size_query_param = 'page_size'
    max_page_size = 100


class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] #Allows any user to view posts.

    pagination_class = StandardResultsSetPagination

    # Attaching the pagination class
    pagination_class = StandardResultsSetPagination
    
    # Enable filtering, search, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # Filtering will allow clients to filter by author or creation date (for example)
    filterset_fields = ['author', 'created_at']
    
    # Search by title or content (clients can send ?search=keyword)
    search_fields = ['title', 'content']
    
    # Allow ordering by creation or update time
    ordering_fields = ['created_at', 'updated_at']


    def perform_create(self, serializer):
        # Automatically sets the current user as the author when creating a post.
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]#Allows only authenticated users to view posts.

    pagination_class = StandardResultsSetPagination

    def perform_create(self, serializer):
        # Automatically sets the current user as the author when creating a comment.
        serializer.save(author=self.request.user)

