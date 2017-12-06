from rest_framework import serializers

from .models import SMSMessage

__all__ = (
    'SMSMessageSerializer',
    'SMSReceiveMessageSerializer',
    'SMSReceiveTrustcoMessageSerializer',
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

    # 'user': 'Authentication Failed',
    # 'password': 'Authentication Failed',
    # 'MSISDN': 'Missing MSISDN',
    # 'shortCode': 'Missing Source Address',
    # 'MESSAGE': 'Missing Message Content',
    # 'messageID': 'uuid',

    user = serializers.CharField(required=True)
    MSISDN = serializers.CharField(required=True)
    shortCode = serializers.CharField(required=True)
    MESSAGE = serializers.CharField(required=True)
    messageID = serializers.CharField(required=True)

    def __init__(self, *args, **kwargs):
        super(SMSReceiveMessageSerializer, self).__init__(*args, **kwargs)
        self.fields['pass'] = serializers.CharField(required=True)

    class Meta(object):
        """Meta options."""

        model = SMSMessage
        fields = (
            'user',
            'pass',
            'MSISDN',
            'shortCode',
            'MESSAGE',
            'messageID',
        )

    def build_unknown_field(self, field_name, model_class):
        if field_name == 'pass':
            return self.build_property_field('pass_', model_class)
        else:
            super(SMSReceiveMessageSerializer, self).build_unknown_field(
                field_name,
                model_class
            )


class SMSReceiveTrustcoMessageSerializer(
    serializers.HyperlinkedModelSerializer
):
    """SMSMessage serializer used in the receive_message action."""

    Message = serializers.CharField(source='message')
    DateFrom = serializers.DateTimeField(source='arrival_date')
    FromShortCode = serializers.CharField(required=True, source='sender')
    Priority = serializers.CharField(source='priority')

    # def __init__(self, *args, **kwargs):
    #     super(SMSReceiveTrustcoMessageSerializer, self).__init__(*args, **kwargs)
    #     # self.fields['pass'] = serializers.CharField(required=True)

    class Meta(object):
        """Meta options."""

        model = SMSMessage
        fields = (
            'Message',
            'DateFrom',
            'FromShortCode',
            'Priority',
        )
