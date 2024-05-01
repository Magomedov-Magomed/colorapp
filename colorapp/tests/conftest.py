import pytest
from django.urls import reverse
from users.models import User


@pytest.fixture
def user():
    return User.objects.create_user(username='test', password='test', name='test')


@pytest.fixture
def auth_token(user, client):
    auth_url = reverse('token_obtain_pair')
    resp = client.post(auth_url, data={"username": user.username, "password": 'test'})
    resp_data = resp.json()
    access = resp_data['access']
    return access
