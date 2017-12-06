from django.db import models
from django.utils.translation import ugettext_lazy as _

from .constants import (
    SMS_MESSAGE_DELIVERY_STATUSES,
    SMS_MESSAGE_DELIVERY_STATUS_SENT,
    SMS_MESSAGE_PRIORITIES,
    SMS_MESSAGE_PRIORITY_NORMAL,
)

__all__ = ('SMSMessage',)


@property
def _pass(self):
    return ''


attrs = {
    'name': _pass,
    '__module__': 'sms.models'
}
PassMixin = type("PassMixin", (object,), attrs)


class SMSMessage(models.Model, PassMixin):
    """Message model.

    As it's described in the `The DMS Receive SMS Interface - HTTP Post`,
    the message should consist of the following fields:

        to - The cell number (or a short code) on which the SMS was received.
        from - The cell number from which the SMS was received.
        text - The SMS message received.

    We can't preserve the names, because in Python the `from` is reserved word.
    Moreover, to make it clear, we make the following logical name
    transformations:

        to -> recipient
        from -> sender
        text -> message

    Next to that, we record the time message was delivered and assign a
    unique number to the message (uuid field).
    """

    uuid = models.UUIDField(
        verbose_name=_("Unique identifier"),
        editable=True,
        unique=True
    )
    recipient = models.TextField(
        verbose_name=_("Recipient"),
        help_text=_("The `to` field in the DMS Receive SMS Interface")
    )
    sender = models.CharField(
        verbose_name=_("Sender"),
        max_length=255,
        help_text=_("The `from` field in the DMS Receive SMS Interface")
    )
    message = models.TextField(
        verbose_name=_("Message"),
        help_text=_("The `text` field in the DMS Receive SMS Interface")
    )
    date_created = models.DateTimeField(
        verbose_name=_("Date created"),
        auto_now_add=True,
        help_text=_("Date created.")
    )
    delivery_status = models.CharField(
        verbose_name=_("Delivery status"),
        max_length=255,
        choices=SMS_MESSAGE_DELIVERY_STATUSES,
        default=SMS_MESSAGE_DELIVERY_STATUS_SENT,
        help_text=_("Message delivery status (if known)")
    )
    date_delivered = models.DateTimeField(
        verbose_name=_("Date delivered"),
        null=True,
        blank=True,
        help_text=_("Date delivered.")
    )
    priority = models.IntegerField(
        verbose_name=_("Priority"),
        null=True,
        blank=True,
        choices=SMS_MESSAGE_PRIORITIES,
        default=SMS_MESSAGE_PRIORITY_NORMAL,
        help_text=_("The `from` field in the SMS Receive SMS Interface")
    )
    arrival_date = models.DateTimeField(
        verbose_name=_("Arrival date"),
        null=True,
        blank=True,
        help_text=_("Date when the SMS message needs to be sent on.")
    )

    class Meta(object):
        """Meta options."""

        verbose_name = _("SMS message")
        verbose_name_plural = _("SMS messages")
        ordering = ["-date_created"]

    def __str__(self):
        return self.message
