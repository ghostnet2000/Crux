import uuid

from drf_custom_viewsets.viewsets import CustomSerializerViewSet

from rest_framework import status
from rest_framework.decorators import list_route
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import SMSMessage
from .serializers import (
    AuthenticateSerializer,
    SMSMessageSerializer,
    SMSReceiveMessageSerializer,
)

__all__ = ('SMSMessageViewSet',)


class SMSMessageViewSet(CustomSerializerViewSet):
    """SMSMessage ViewSet."""

    queryset = SMSMessage.objects.all()
    serializer_class = SMSMessageSerializer
    custom_serializer_classes = {
        'authenticate': AuthenticateSerializer,
        'receive_message': SMSReceiveMessageSerializer,
    }
    permission_classes = [AllowAny]

    @list_route(methods=['get'])
    def authenticate(self, request):
        request_data = request.query_params.copy()
        serializer = AuthenticateSerializer(
            data=request_data,
            context={'request': request}
        )

        is_valid = serializer.is_valid(raise_exception=False)
        if is_valid:
            headers = self.get_success_headers(serializer.data)
            return Response(
                data={'SID': uuid.uuid4()},
                status=status.HTTP_200_OK,
                headers=headers
            )
        else:
            raise ValidationError(serializer.errors)

    @list_route(methods=['get'])
    def receive_message(self, request):
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
        request_data = request.query_params.copy()
        recipients = []

        for counter in range(0, len(request.query_params)):
            _field_name = 'numbers[{}]'.format(counter)
            if _field_name in request_data:
                _value = request_data.get(_field_name)
                request_data.pop(_field_name)
                recipients.append(_value)

        request_data['recipient'] = ', '.join(recipients)

        # serializer = self.get_serializer()
        serializer = SMSReceiveMessageSerializer(
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
            raise ValidationError(serializer.errors)
