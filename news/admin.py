from django.contrib import admin
from .models import News, UserImage, Comment


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    """Новини"""
    list_display = ("id", "title")
    list_display_links = ("id", "title")
    search_fields = ("title",)
    readonly_fields = ("view",)


@admin.register(UserImage)
class UserImageAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ("like",)
