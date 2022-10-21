import pytest
from django.contrib.auth import get_user_model

from url_trimmer.models import SaveURL


@pytest.fixture(scope='function')
def user(db, django_user_model):
    """
    User instance from default user model and Address instance from `users.models`
    that is necessary to create a User object.
    """

    user = django_user_model.objects.create_user(
        password='12345',
        username='Happy Horses',
        email='office@happyhorses.pl',
    )
    yield user


@pytest.fixture(scope='function')
def new_url(db):
    user = get_user_model().objects.get(pk=1)
    new_url = SaveURL.objects.create(
        url='jetbrains.com',
        user=user
    )

    yield new_url
