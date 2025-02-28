from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()


class CustomUserManager(BaseUserManager):
     
     def create_user(self, username, email, date_of_birth,  password=None, **extra_fields):
        if not email:
            raise ValueError("Please set the Email Field")
        
        email = self.normalize_email(email)
    
        user = self.model(username=username, email=email, date_of_birth=date_of_birth, **extra_fields)
        user.set_password(password)
        
        return user
     

     def create_superuser(self, username, email, date_of_birth, password=None, **extra_fields):
      
        if not email:
            raise ValueError('Please set the Email Field')

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError('Superuser must be staff')
        if not extra_fields.get('is_superuser'):
            raise ValueError('Superuser must be SuperUser.')

        return self.create_user(username, email, date_of_birth, password, **extra_fields)
     



class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(blank=True)

    objects = CustomUserManager()

    
