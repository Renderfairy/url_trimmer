import pytest


@pytest.fixture(scope='function')
def user(db, django_user_model):
    """
    User instance from default user model and Address instance from 'users.models'
    that is necessary to create a User object.
    """

    user = django_user_model.objects.create_user(
        password='12345',
        username='Happy Horses',
        email='office@happyhorses.pl',
    )
    yield user
