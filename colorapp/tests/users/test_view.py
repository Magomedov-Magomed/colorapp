import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_login_view(user, client):
    login_url = reverse('token_obtain_pair')
    resp = client.post(login_url, data={"username": user.username, "password": 'test'})
    assert resp.status_code == 200
    resp_data = resp.json()
    access, refresh = resp_data['access'], resp_data['refresh']
    assert access, refresh

    # change access
    login_url = reverse('token_refresh')
    resp = client.post(login_url, data={'refresh': refresh})
    assert resp.status_code == 200
    resp_data = resp.json()
    new_access = resp_data['access']
    assert access != new_access
