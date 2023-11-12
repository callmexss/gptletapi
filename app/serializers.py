from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import App, GPTEntry, Comment


User = get_user_model()


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ["id", "name", "author", "description"]
        read_only_fields = ["id", "author"]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'text', 'created_at', 'updated_at', 'parent']


class GPTEntrySerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = GPTEntry
        fields = ["id", "name", "description", "category", "image_url", "link_url", "comments"]
        read_only_fields = ["id", "upvote", "downvote", "comments"]


class URLSerializer(serializers.Serializer):
    url = serializers.URLField()
    generate_category = serializers.BooleanField(default=False)
