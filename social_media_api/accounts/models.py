from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    bio = models.TextField(max_length=280)
    profile_picture = models.ImageField(blank=True, null=True)
    followers = models.ManyToManyField('self',
                                        symmetrical=False,
                                         blank=True,
                                         related_name='following_set')
    
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='followers_set',
        blank=True
    )


    def __str__(self):
        return self.username