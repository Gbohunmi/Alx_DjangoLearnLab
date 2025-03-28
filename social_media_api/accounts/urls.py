from django.urls import path
from .views import RegistrationAPIView, LoginAPIView, UserProfileAPIView, FollowAPIView, UnfollowAPIView

urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name='registration'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('profile/', UserProfileAPIView.as_view(), name='profile'),
    path('follow/<int:user_id>/', FollowAPIView.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', UnfollowAPIView.as_view(), name='unfollow-user'),

]
