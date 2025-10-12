from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from notifications.models import Notification

User = get_user_model()

@receiver(m2m_changed, sender=User.following.through)
def create_follow_notification(sender, instance, action, pk_set, **kwargs):
    if action == "post_add":
        for target_id in pk_set:
            try:
                target = User.objects.get(pk=target_id)
            except User.DoesNotExist:
                continue
            if target != instance:
                Notification.objects.create(
                    recipient=target,
                    actor=instance,
                    verb="followed you",
                )
