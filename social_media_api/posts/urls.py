from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedAPIView, LikePostAPIView, UnlikePostAPIView

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', FeedAPIView.as_view(), name='feed'),
    path('like/<int:post_id>/', LikePostAPIView.as_view(), name='like-post'),
    path('unlike/<int:post_id>/', UnlikePostAPIView.as_view(), name='unlike-post'),

]
