from django.contrib.auth import get_user_model
from django.urls import reverse


def test_user_can_register(client, user):
    url = reverse('users:register')
    client.post(url, data={
        'username': 'TestUserName',
        'email': 'test@email.com',
        'password': 'muchstrongpassword',
        'password2': 'muchstronpassowrd',
    })

    assert len(get_user_model().objects.all()) == 2