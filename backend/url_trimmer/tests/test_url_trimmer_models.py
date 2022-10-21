from django.contrib.auth import get_user_model

from url_trimmer.models import SaveURL


def test_dd_url(new_url, user):
    users = get_user_model().objects.all()
    urls = SaveURL.objects.all()
    assert len(urls) == 1
    assert len(users) == 2
