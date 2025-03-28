from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from .serializers import RegistrationSerializer, LoginSerializer, UserProfileSerializer
from rest_framework.generics import RetrieveUpdateAPIView
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, status

User = get_user_model()


# Create your views here.

class RegistrationAPIView(APIView):
    # Allows anyone to access this view 
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            # Saves the user, which also creates their token as defined in the serializer
            user = serializer.save()
            # Retrieves the token created for the user
            token = Token.objects.get(user=user)
            return Response({
                "message": "User Registration Successful.",
                "user": serializer.data,
                "token": token.key
            }, status=status.HTTP_201_CREATED)
        return Response({"message": "User Registration Failed."},
                            status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    permission_classes = [AllowAny]  

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            
            # Retrieve or create an authentication token for the user
            token, created = Token.objects.get_or_create(user=user)

            return Response({
                "token": token.key,
                "username": user.username,
                "email": user.email
            }, status=status.HTTP_200_OK)

        # Returns validation errors if provided data is invalid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileAPIView(RetrieveUpdateAPIView):
    """
    This view allows authenticated users to retrieve (GET)
    and update (PUT/PATCH) their own profile information.
    """
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # Returns the currently authenticated user
        # ensures users can only access their own profile.
        return self.request.user


class FollowAPIView(generics.GenericAPIView):
    """
    Allows an authenticated user to follow another user.
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id, *args, **kwargs):
        """
        Expects the URL to provide the target user's ID as 'user_id'.
        """
        try:
            target_user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response(
                {'detail': 'User not found.'},
                status=status.HTTP_404_NOT_FOUND
            )

        # Prevent self-following
        if target_user == request.user:
            return Response(
                {'detail': 'You cannot follow yourself.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Check if the request.user is already following the target user.
        if target_user in request.user.following.all():
            return Response(
                {'detail': 'You are already following this user.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Add the target user to the authenticated user's following list.
        request.user.follower.add(target_user)
        
        return Response(
            {'detail': f'You are now following {target_user.username}.'},
            status=status.HTTP_200_OK
        )

class UnfollowAPIView(generics.GenericAPIView):
    """
    Allows an authenticated user to unfollow a user.
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id, *args, **kwargs):
        """
        Expects the URL to provide the target user's ID as 'user_id'.
        """
        try:
            target_user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response(
                {'detail': 'User not found.'},
                status=status.HTTP_404_NOT_FOUND
            )

        # Checks that the user is actually following the target, otherwise there is nothing to unfollow.
        if target_user not in request.user.following.all():
            return Response(
                {'detail': 'You are not following this user.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Removes the target user from the authenticated user's following list.
        request.user.following.remove(target_user)
        return Response(
            {'detail': f'You have unfollowed {target_user.username}.'},
            status=status.HTTP_200_OK
        )

#CustomUser.objects.all()