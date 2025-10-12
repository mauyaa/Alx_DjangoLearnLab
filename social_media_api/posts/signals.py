from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Like, Comment
from notifications_app.models import Notification

@receiver(post_save, sender=Like)
def like_notification(sender, instance, created, **kwargs):
    if created:
        post = instance.post
        if instance.user != post.author:
            Notification.objects.create(
                recipient=post.author,
                actor=instance.user,
                verb='liked your post',
                target_content_type=None,
                target_object_id=None,
                target_object=None,
            )

@receiver(post_save, sender=Comment)
def comment_notification(sender, instance, created, **kwargs):
    if created:
        post = instance.post
        if instance.author != post.author:
            Notification.objects.create(
                recipient=post.author,
                actor=instance.author,
                verb='commented on your post',
                target_content_type=None,
                target_object_id=None,
                target_object=None,
            )
