from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import App, GPTEntry


User = get_user_model()


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ["id", "name", "author", "description"]
        read_only_fields = ["id", "author"]


class GPTEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = GPTEntry
        fields = ["id", "name", "description", "image_url", "link_url"]
        read_only_fields = ["id"]
