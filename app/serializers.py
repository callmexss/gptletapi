from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import App, GPTEntry, Comment, EntryVote


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
    upvotes = serializers.SerializerMethodField()
    downvotes = serializers.SerializerMethodField()

    class Meta:
        model = GPTEntry
        fields = ["id", "name", "description", "category", "image_url", "link_url", "unique_link_url", "comments", "upvotes", "downvotes"]
        read_only_fields = ["id", "upvotes", "downvotes", "comments"]

    def get_upvotes(self, obj):
        return EntryVote.objects.filter(entry=obj, is_upvote=True).count()

    def get_downvotes(self, obj):
        return EntryVote.objects.filter(entry=obj, is_upvote=False).count()


class URLSerializer(serializers.Serializer):
    url = serializers.URLField()
    generate_category = serializers.BooleanField(default=False)
