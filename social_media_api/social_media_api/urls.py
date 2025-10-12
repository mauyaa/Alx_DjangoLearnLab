from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),  # ✅ register/login/profile + follow routes
    path("", include("posts.urls")),              # ✅ feed + like/unlike
]
