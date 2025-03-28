from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from rest_framework import generics
from rest_framework import permissions
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType
from rest_framework.response import Response
from rest_framework import status


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

class FeedAPIView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Get the current logged-in user.
        user = self.request.user

        # Retrieves all users that 'user' is following.
        
        following_users = user.following.all()

        # Fetch posts authored by these followed users.
        # Order by creation date descending so the most recent posts appear first.
        queryset = Post.objects.filter(author__in=following_users).order_by('-created_at')
        return queryset

class LikePostAPIView(generics.APIView):
    """
    Handles liking a post.
    Prevents duplicate likes and generates a notification for the action.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, post_id, *args, **kwargs):
        post = generics.get_object_or_404(Post, pk=post_id)

        # Check if the user has already liked the post
        if Like.objects.filter(post=post, user=request.user).exists():
            return Response(
                {'detail': 'You have already liked this post.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Create a Like entry
        like = Like.objects.create(post=post, user=request.user)

        # Generate a notification for the like
        content_type = ContentType.objects.get_for_model(post)
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb='liked',
            target_content_type=content_type,
            target_object_id=post.id
        )

        return Response(
            {'detail': 'You have liked the post.', 'like_id': like.id},
            status=status.HTTP_201_CREATED
        )


class UnlikePostAPIView(generics.APIView):
    """
    Handles unliking a post.
    Removes the like entry from the database.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, post_id, *args, **kwargs):
        post = generics.get_object_or_404(Post, pk=post_id)

        # Check if the user has liked the post
        try:
            like = Like.objects.get(post=post, user=request.user)
        except Like.DoesNotExist:
            return Response(
                {'detail': 'You have not liked this post.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Delete the Like entry
        like.delete()

        return Response(
            {'detail': 'You have unliked the post.'},
            status=status.HTTP_200_OK
        )

