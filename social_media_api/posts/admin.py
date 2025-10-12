from django.contrib import admin
from .models import Post, Like

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'body', 'created_at')
    search_fields = ('body', 'author__username')

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'user', 'created_at')
    search_fields = ('post__body', 'user__username')
