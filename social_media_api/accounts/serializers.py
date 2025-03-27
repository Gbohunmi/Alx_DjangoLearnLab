from rest_framework import serializers

from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed


#Serializer to create new accounts
class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)


    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password', 'bio', 'profile_picture']

    def create(self, validated_data):
        # Creates a user with provided data
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            bio=validated_data.get('bio', None),
            profile_picture=validated_data.get('profile_picture', None))
        
        # Creates authentication token for the user   
        Token.objects.create(user=user)
        return user

    #Enforces Email uniqueness
    def validate_email(self, value):
        if get_user_model().objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True, required=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            # Authenticates user using Django's built-in authentication
            user = authenticate(username=username, password=password)
            if not user:
                raise AuthenticationFailed("Invalid username or password.")
            data['user'] = user  # Adds user object to validated data
        else:
            raise serializers.ValidationError("Both username and password are required.")

        return data

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        # Included the fields that users are allowed to view and update.
        
        fields = ['username', 'email', 'bio', 'profile_picture', 'followers']
        extra_kwargs = {      
            'email': {'read_only': True},
            'followers': {'read_only': True},
        }
