from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import User
from notifications_app.models import Notification

@receiver(m2m_changed, sender=User.following.through)
def create_follow_notification(sender, instance, action, pk_set, **kwargs):
    # instance is the actor (the follower); pk_set are target user ids
    if action == 'post_add':
        for target_id in pk_set:
            try:
                target = User.objects.get(pk=target_id)
            except User.DoesNotExist:
                continue
            if target != instance:
                Notification.objects.create(
                    recipient=target,
                    actor=instance,
                    verb='followed you',
                    target_object=None,  # follow has no concrete object target
                )
