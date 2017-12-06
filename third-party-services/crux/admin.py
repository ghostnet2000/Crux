from django.contrib import admin

from .models import SMSMessage

__all__ = ('SMSMessageAdmin',)


@admin.register(SMSMessage)
class SMSMessageAdmin(admin.ModelAdmin):
    """SMSMessage admin."""

    list_display = (
        'id',
        'uuid',
        'sender',
        'recipient',
        'message',
        'date_created',
        'delivery_status',
        'date_delivered',
    )
    fields = (
        'id',
        'uuid',
        'sender',
        'recipient',
        'message',
        'date_created',
        'delivery_status',
        'date_delivered',
    )
    search_fields = (
        'sender',
        'recipient',
        'message'
    )
    readonly_fields = (
        'id',
        'uuid',
        'date_created',
        'delivery_status',
        'date_delivered',
    )
