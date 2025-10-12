from django.urls import path
from .views import FeedView, LikePostView, UnlikePostView

urlpatterns = [
    path("feed/", FeedView.as_view(), name="feed"),                 # ✅ /feed/
    path("posts/<int:pk>/like/", LikePostView.as_view(), name="like-post"),     # ✅ like
    path("posts/<int:pk>/unlike/", UnlikePostView.as_view(), name="unlike-post")# ✅ unlike
]
