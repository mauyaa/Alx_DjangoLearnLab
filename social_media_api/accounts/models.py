from django.db import models
from django.contrib.auth.models import AbstractUser

def user_profile_upload_path(instance, filename):
    return f"profiles/user_{instance.id}/{filename}"

class User(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to=user_profile_upload_path, blank=True, null=True)
    # Users this user is following
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)

    def __str__(self):
        return self.username
