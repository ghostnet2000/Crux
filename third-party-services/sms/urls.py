from rest_framework_extensions.routers import ExtendedDefaultRouter

from .viewsets import SMSMessageViewSet

__all__ = ('urlpatterns',)


router = ExtendedDefaultRouter()
router.register(r'sms', SMSMessageViewSet, base_name='smsmessage')

urlpatterns = router.urls
