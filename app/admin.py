from django.contrib import admin
from .models import App, GPTEntry, Category, Tag


@admin.register(App)
class AppAdmin(admin.ModelAdmin):
    list_display = ("name", "author", "created_at", "updated_at")
    search_fields = ("name", "author")
    list_filter = ("created_at", "updated_at")
    ordering = ("-created_at",)


@admin.register(GPTEntry)
class GPTEntryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'description', 'link_url', 'image_url')
    search_fields = ('name', 'description')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)
