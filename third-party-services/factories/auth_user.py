from django.conf import settings

from factory import (
    DjangoModelFactory,
    PostGenerationMethodCall,
    Sequence,
)

from factory import Faker

__all__ = (
    'TEST_ADMIN_USER',
    'TEST_API_USER',
    'TEST_USER',
    'TEST_ADMIN_USER',
    'TEST_PASSWORD',
    'TestApiUserFactory',
    'TestUserFactory',
    'TestStaffUserFactory',
    'TestAdminUserFactory',
    'UserFactory',
)

TEST_USER = 'test_user'
TEST_API_USER = 'test_api_user'
TEST_STAFF_USER = 'test_staff'
TEST_ADMIN_USER = 'test_admin'
TEST_PASSWORD = 'test_password'


class AbstractUserFactory(DjangoModelFactory):
    """Abstract factory for creating users."""

    password = PostGenerationMethodCall('set_password', TEST_PASSWORD)
    username = Sequence(lambda n: 'user%d' % n)
    first_name = Faker('first_name')
    last_name = Faker('last_name')
    email = Faker('email')

    is_active = False
    is_staff = False
    is_superuser = False

    class Meta(object):
        """Meta options."""

        model = settings.AUTH_USER_MODEL
        django_get_or_create = ('username',)
        abstract = True


class UserFactory(AbstractUserFactory):
    """Factory for creating users."""


class TestUserFactory(AbstractUserFactory):
    """Factory for creating basic user `test_user`."""

    username = TEST_USER
    is_active = True


class TestApiUserFactory(AbstractUserFactory):
    """Factory for creating basic user `test_api_user`."""

    username = TEST_API_USER
    is_active = True


class TestStaffUserFactory(AbstractUserFactory):
    """Factory for creating staff (admin) user `test_staff`."""

    username = TEST_STAFF_USER
    is_active = True
    is_staff = True


class TestAdminUserFactory(AbstractUserFactory):
    """Factory for creating super admin user `test_admin`."""

    username = TEST_ADMIN_USER
    is_active = True
    is_staff = True
    is_superuser = True
