from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import App


User = get_user_model()


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ['id', 'name', 'author', 'description']
        read_only_fields = ['id', 'author']
