import pytest
from django.urls import reverse
from url_trimmer.models import SaveURL


@pytest.mark.django_db
def test_link_detail_view_404(client):
    url = reverse('url_trimmer:link_detail', kwargs={'link_id': 1})
    response = client.get(url)
    assert response.status_code == 200
    assert "h1>Page with given address doesn't exist</h1>" in response.content.decode('UTF-8')


@pytest.mark.django_db
def test_link_detail_view(client, new_url):
    url = reverse('url_trimmer:link_detail', kwargs={'link_id': new_url.id})
    response = client.get(url)
    assert response.status_code == 200
    assert new_url.url in response.content.decode('UTF-8')


@pytest.mark.django_db
def test_link_redirect_view(client, new_url):
    url = reverse('url_trimmer:link_redirect', kwargs={'alias': new_url.alias})
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_link_delete_view(client, new_url):
    url = reverse('url_trimmer:link_delete', kwargs={'alias': new_url.alias})
    response = client.get(url)

    assert response.status_code == 302
    assert SaveURL.objects.all().count() == 0
