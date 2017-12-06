from factory import DjangoModelFactory

from sms.models import SMSMessage

from factory import Faker

__all__ = ('SMSMessageFactory',)


class BaseSMSMessageFactory(DjangoModelFactory):
    """Base SMSMessage factory."""

    recipient = Faker('phone_number')
    sender = Faker('phone_number')
    message = Faker('sentence')

    class Meta(object):
        """Meta class."""

        model = SMSMessage
        abstract = True
        django_get_or_create = ('id',)


class SMSMessageFactory(BaseSMSMessageFactory):
    """SMSMessage factory."""
