from django.contrib import admin
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'recipient', 'actor', 'verb', 'timestamp')
    search_fields = ('verb', 'recipient__username', 'actor__username')
    list_filter = ('timestamp',)
