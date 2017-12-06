from drf_custom_viewsets.viewsets import CustomSerializerViewSet

from rest_framework import status
from rest_framework.decorators import list_route
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import SMSMessage
from .serializers import (
    SMSMessageSerializer,
    SMSReceiveMessageSerializer,
    SMSReceiveTrustcoMessageSerializer,
)

__all__ = ('SMSMessageViewSet',)


PARAMS_MAPPING = {
    'MSISDN': 'recipient',
    'shortCode': 'sender',
    'MESSAGE': 'message',
    'messageID': 'uuid',
}

ERROR_MESSAGES = {
    'user': 'Authentication Failed',
    'pass': 'Authentication Failed',
    'MSISDN': 'Missing MSISDN',
    'shortCode': 'Missing Source Address',
    'MESSAGE': 'Missing Message Content',
    'messageID': 'uuid',
}

USER_PARAM = 'test_user'
PASSWORD_PARAM = 'test_password'


class SMSMessageViewSet(CustomSerializerViewSet):
    """SMSMessage ViewSet."""

    queryset = SMSMessage.objects.all()
    serializer_class = SMSMessageSerializer
    custom_serializer_classes = {
        'receive_message': SMSReceiveMessageSerializer,
        'receive_trustco_message': SMSReceiveTrustcoMessageSerializer,
    }
    permission_classes = [AllowAny]

    @list_route(methods=['get', 'post'])
    def receive_message(self, request):
        """Receive message example

        Sample request:

            http://ke.mtechcomm.com/bulkAPIV2/?
                user=demoUser&
                pass=demoPassword&
                messageID=msgID&
                shortCode=DEMOSOURCEADDR&
                MSISDN=254722000000&
                MESSAGE=This+is+an+Mtech+API+test+Message

        Sample Response

            200 Successfully Submitted Message [msgID] to MTech

        :param request:
        :return:
        """
        data = {}
        _missing_params = []

        request_data = request.data if request.method == 'POST' else request.GET

        for _source_param, _destination_param in PARAMS_MAPPING.items():
            _value = request_data.get(_source_param, '')
            if _value:
                data.update({_destination_param: _value})
            else:
                _missing_params.append(_source_param)

        if _missing_params:
            raise ValidationError(
                detail='The following params are empty: {}.'.format(
                    ', '.join(_missing_params)
                )
            )

        serializer = SMSMessageSerializer(
            data=data,
            context={'request': request}
        )
        is_valid = serializer.is_valid(raise_exception=False)
        if is_valid:
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            content = "Successfully Submitted Message {} to MTech".format(
                request_data.get('messageID', '')
            )
            return Response(
                data=content,
                status=status.HTTP_200_OK,
                headers=headers
            )
        else:
            _serializer = SMSReceiveMessageSerializer(
                data=request.data,
                context={'request': request}
            )
            _serializer.is_valid(raise_exception=False)
            _serializer._errors = serializer._errors
            raise ValidationError(_serializer.errors)

    @list_route(methods=['get'])
    def receive_trustco_message(self, request):
        """Receive message example

        Sample request:

            http://www.sms.na/api/SMS/SendSMS
                ?SID={SID}
                &Message={Message}
                &DateFrom={DateFrom}
                &FromShortCode={FromShortCode}
                &Priority={Priority}
                &numbers[0]={numbers[0]}
                &numbers[1]={numbers[1]}
                &numbers[2]={numbers[2]}

        Sample Response

            200

        :param request:
        :return:
        """
        data = {}

        request_data = request.query_params.copy()
        recipients = []

        for counter in range(0, len(request.query_params)):
            _field_name = 'numbers[{}]'.format(counter)
            if _field_name in request_data:
                _value = request_data.get(_field_name)
                request_data.pop(_field_name)
                recipients.append(_value)
        # import ipdb; ipdb.set_trace()
        request_data['recipient'] = ', '.join(recipients)
        print(request_data)
        # serializer = self.get_serializer()
        serializer = SMSReceiveTrustcoMessageSerializer(
            data=request_data,
            context={'request': request}
        )
        is_valid = serializer.is_valid(raise_exception=False)
        if is_valid:
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            content = "Successfully Submitted Message {} to Trustco".format(
                request_data.get('uuid', '')
            )
            return Response(
                data=content,
                status=status.HTTP_200_OK,
                headers=headers
            )
        else:
            # _serializer = SMSReceiveTrustcoMessageSerializer(
            #     data=data,
            #     context={'request': request}
            # )
            # _serializer.is_valid(raise_exception=False)
            # _serializer._errors = serializer._errors
            raise ValidationError(serializer.errors)
