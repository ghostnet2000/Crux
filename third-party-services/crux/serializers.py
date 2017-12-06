from rest_framework import serializers

from .models import SMSMessage

__all__ = (
    'AuthenticateSerializer',
    'SMSMessageSerializer',
    'SMSReceiveMessageSerializer',
)


class AuthenticateSerializer(serializers.Serializer):
    """Authentication serializer."""

    Username = serializers.CharField(required=True)
    Password = serializers.CharField(required=True)

    class Meta(object):
        """Meta options."""

        fields = (
            'Username',
            'Password',
        )


class SMSMessageSerializer(serializers.HyperlinkedModelSerializer):
    """SMSMessage serializer."""

    class Meta(object):
        """Meta options."""

        model = SMSMessage
        fields = (
            'url',
            'id',
            'uuid',
            'sender',
            'recipient',
            'message',
            'date_created',
            'delivery_status',
            'date_delivered',
        )
        read_only_fields = (
            'id',
        )


class SMSReceiveMessageSerializer(serializers.HyperlinkedModelSerializer):
    """SMSMessage serializer used in the receive_message action."""

    Message = serializers.CharField(source='message')
    DateFrom = serializers.DateTimeField(source='arrival_date')
    FromShortCode = serializers.CharField(required=True, source='sender')
    Priority = serializers.CharField(source='priority')

    class Meta(object):
        """Meta options."""

        model = SMSMessage
        fields = (
            'uuid',
            'Message',
            'DateFrom',
            'FromShortCode',
            'Priority',
        )
