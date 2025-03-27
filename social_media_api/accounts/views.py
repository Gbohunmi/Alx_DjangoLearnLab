from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from .serializers import RegistrationSerializer, LoginSerializer, UserProfileSerializer
from rest_framework.generics import RetrieveUpdateAPIView

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


