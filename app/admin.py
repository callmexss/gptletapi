from django.contrib import admin
from .models import App, GPTEntry


@admin.register(App)
class AppAdmin(admin.ModelAdmin):
    list_display = ("name", "author", "created_at", "updated_at")
    search_fields = ("name", "author")
    list_filter = ("created_at", "updated_at")
    ordering = ("-created_at",)


@admin.register(GPTEntry)
class GPTEntryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image_url', 'link_url')
    search_fields = ('name',)
