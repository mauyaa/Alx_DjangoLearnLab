from rest_framework import serializers

from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    actor_username = serializers.ReadOnlyField(source="actor.username")
    target_type = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = [
            "id",
            "recipient",
            "actor",
            "actor_username",
            "verb",
            "timestamp",
            "unread",
            "target_id",
            "target_type",
        ]
        read_only_fields = ["recipient", "actor", "verb", "timestamp", "unread", "target_id", "target_type"]

    def get_target_type(self, obj):
        return obj.target_ct.model if obj.target_ct else None
