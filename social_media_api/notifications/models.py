from django.db import models
from django.conf import settings

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


# Create your models here.

class Notification(models.Model):
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, 
                                  on_delete=models.CASCADE, 
                                  related_name='notifications'
                                  )
    actor = models.ForeignKey(settings.AUTH_USER_MODEL, 
                              on_delete=models.CASCADE, 
                              related_name='actor_notifications'
                              )
    verb = models.CharField(max_length=255)  # A brief description of the action, e.g., 'liked', 'commented'

    target_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    target_object_id = models.PositiveIntegerField()
    target = GenericForeignKey('target_content_type', 'target_object_id')
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.actor.username} {self.verb} {self.target}"
