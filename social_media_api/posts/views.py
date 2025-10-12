from django.contrib.contenttypes.models import ContentType
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post, Like
from .serializers import PostSerializer  # create a simple serializer with fields = ["id","author","body","created_at"]
from notifications.models import Notification

class FeedView(generics.ListAPIView):  # ✅ feed: posts from users current user follows
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        following_ids = user.following.values_list("id", flat=True)
        return Post.objects.filter(author_id__in=following_ids).order_by("-created_at")  # ✅ ordered newest first


class LikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)
        like, created = Like.objects.get_or_create(post=post, user=request.user)
        if created:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked your post",
                target_ct=ContentType.objects.get_for_model(Post),
                target_id=post.id,
            )
        return Response({"detail": "Liked"}, status=200)


class UnlikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)
        Like.objects.filter(post=post, user=request.user).delete()
        return Response({"detail": "Unliked"}, status=200)
