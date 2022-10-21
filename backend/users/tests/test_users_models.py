def test_create_user(user, django_user_model):
    users = django_user_model.objects.all()

    assert len(users) == 2