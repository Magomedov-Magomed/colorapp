import pytest
from users.models import User
from users.services import UserService


@pytest.mark.django_db
def test_create_user():
    users = User.objects.all()
    assert not users
    user_service = UserService()
    data = {"name": 'test', "username": 'test', 'password': 'test'}
    user = user_service.create_user(data)
    assert User.objects.first() == user
