from django.urls import path
from .views import RegistrationAPIView, LoginAPIView, UserProfileAPIView

urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name='registration'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('profile/', UserProfileAPIView.as_view(), name='profile'),
]
