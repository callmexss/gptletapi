from django.contrib import admin
from .models import App


class AppAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'created_at', 'updated_at')
    search_fields = ('name', 'author')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)

admin.site.register(App, AppAdmin)
