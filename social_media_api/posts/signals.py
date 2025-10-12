from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Like
from notifications.models import Notification

@receiver(post_save, sender=Like)
def like_notification(sender, instance, created, **kwargs):
    if created:
        post = instance.post
        if instance.user != post.author:
            Notification.objects.create(
                recipient=post.author,
                actor=instance.user,
                verb="liked your post",
            )
