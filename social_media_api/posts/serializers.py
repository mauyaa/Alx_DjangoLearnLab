from rest_framework import serializers

from .models import Comment, Post


class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source="author.username")
    likes_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            "id",
            "author",
            "author_username",
            "title",
            "content",
            "created_at",
            "updated_at",
            "likes_count",
            "comments_count",
        ]
        read_only_fields = ["id", "author", "created_at", "updated_at", "likes_count", "comments_count"]

    def get_likes_count(self, obj) -> int:
        return obj.likes.count()

    def get_comments_count(self, obj) -> int:
        return obj.comments.count()


class CommentSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Comment
        fields = [
            "id",
            "post",
            "author",
            "author_username",
            "content",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "author", "created_at", "updated_at", "author_username"]
