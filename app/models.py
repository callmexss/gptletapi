from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


User = get_user_model()


class App(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    description = models.TextField(max_length=10240)
    system_prompt = models.TextField(max_length=10240)
    prompt = models.TextField(max_length=10240)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class GPTEntry(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.URLField(max_length=1024)
    link_url = models.URLField(max_length=1024)

    def __str__(self):
        return self.name
