from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save
from django.dispatch import receiver

from notifications.models import Notification

from .models import Comment, Like


@receiver(post_save, sender=Like)
def like_notification(sender, instance, created, **kwargs):
    if created:
        post = instance.post
        if instance.user != post.author:
            Notification.objects.create(
                recipient=post.author,
                actor=instance.user,
                verb="liked your post",
                target_ct=ContentType.objects.get_for_model(post),
                target_id=post.id,
            )


@receiver(post_save, sender=Comment)
def comment_notification(sender, instance, created, **kwargs):
    if created:
        post = instance.post
        if instance.author != post.author:
            Notification.objects.create(
                recipient=post.author,
                actor=instance.author,
                verb="commented on your post",
                target_ct=ContentType.objects.get_for_model(post),
                target_id=post.id,
            )
