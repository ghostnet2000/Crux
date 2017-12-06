from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

__all__ = ('TrustcoConfig',)


class SMSConfig(AppConfig):
    """Trustco app config."""

    name = 'trustco'
    verbose_name = _("Trustco")
