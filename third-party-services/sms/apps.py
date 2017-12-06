from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

__all__ = ('SMSConfig',)


class SMSConfig(AppConfig):
    """SMS app config."""

    name = 'sms'
    verbose_name = _("SMS")
