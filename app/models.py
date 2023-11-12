from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


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
    description = models.TextField(blank=True, null=True)
    image_url = models.URLField(max_length=1024)
    link_url = models.URLField(max_length=1024)
    unique_link_url = models.URLField(max_length=1024, blank=True, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category_apps", null=True)
    tags = models.ManyToManyField(Tag, related_name="tag_apps", blank=True)
    article = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    entry = models.ForeignKey(GPTEntry, on_delete=models.CASCADE, related_name="comments", db_index=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="replies", db_index=True)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment on {self.entry.name}"

    @property
    def is_reply(self):
        return self.parent is not None

    class Meta:
        indexes = [
            models.Index(fields=['entry', 'parent']),
        ]


class AbstractVote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_upvote = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        unique_together = ('user',)

class EntryVote(AbstractVote):
    entry = models.ForeignKey(GPTEntry, on_delete=models.CASCADE, related_name='votes')

class CommentVote(AbstractVote):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='votes')