from django.contrib.contenttypes.models import ContentType
from rest_framework import filters, generics, permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from notifications.models import Notification

from .models import Comment, Like, Post
from .permissions import IsAuthorOrReadOnly
from .serializers import CommentSerializer, PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["title", "content"]
    ordering_fields = ["created_at", "updated_at"]
    ordering = ["-created_at"]
    filterset_fields = ["author"]

    def get_queryset(self):
        return (
            Post.objects.all()
            .select_related("author")
            .prefetch_related("likes", "comments")
            .all()
        )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def get_queryset(self):
        queryset = Comment.objects.select_related("author", "post").order_by("created_at")
        post_id = self.request.query_params.get("post")
        if post_id:
            queryset = queryset.filter(post_id=post_id)
        return queryset

    def perform_create(self, serializer):
        comment = serializer.save(author=self.request.user)
        post = comment.post
        if post.author != comment.author:
            post_ct = ContentType.objects.get_for_model(post)
            Notification.objects.create(
                recipient=post.author,
                actor=comment.author,
                verb="commented on your post",
                target_ct=post_ct,
                target_id=post.id,
            )


class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        following_users = self.request.user.following.all()
        return (
            Post.objects.filter(author__in=following_users).order_by("-created_at")
            .select_related("author")
            .prefetch_related("likes", "comments")
        )


class LikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if created and post.author != request.user:
            post_ct = ContentType.objects.get_for_model(post)
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked your post",
                target_ct=post_ct,
                target_id=post.id,
            )
        message = "Post liked." if created else "Post already liked."
        return Response({"detail": message}, status=status.HTTP_200_OK)


class UnlikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)
        deleted, _ = Like.objects.filter(post=post, user=request.user).delete()
        if deleted:
            return Response({"detail": "Post unliked."}, status=status.HTTP_200_OK)
        return Response({"detail": "Like not found."}, status=status.HTTP_404_NOT_FOUND)
