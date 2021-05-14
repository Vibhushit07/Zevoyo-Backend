from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Chat(models.Model):
    message = models.TextField()
    posted_at = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'user')
    sentTo = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'sendTo')

    def __str__(self):
        return str(self.message)

    def get_absolute_url(self):
        return reverse("/myApp/chat/all")