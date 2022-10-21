import pytest
from django.urls import reverse


def test_anonymus_user_redirect_from_home_to_login(client):
    url = reverse('users:login')
    response = client.get(url)

    assert response.status_code == 200
    assert '<h1>Login</h1>' in response.content.decode('UTF-8')


@pytest.mark.django_db
def test_authenticated_user_home_page_access(client, user):
    client.force_login(user)
    url = reverse('home:home')
    response = client.get(url)

    assert response.status_code == 200
    assert '<h2>My links</h2>' in response.content.decode('UTF-8')
