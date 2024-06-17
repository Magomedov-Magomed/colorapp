import pytest
from django.test import Client
from django.urls import reverse


@pytest.mark.django_db
def test_palette_crud(client: Client, auth_token):
    # list palettes
    url = reverse('palette-list')
    resp = client.get(url)
    assert resp.status_code == 401
    headers = {'Authorization': f'Bearer {auth_token}'}
    resp = client.get(url, headers=headers)
    assert resp.json() == []

    # create palette
    resp = client.post(url, data={"name": "test_palette"})
    assert resp.status_code == 401
    resp = client.post(url, data={"name": "test_palette"}, headers=headers)
    assert resp.status_code == 201
    created_palette = resp.json()

    # update palette
    url_with_id = url + str(created_palette['id']) + '/'
    resp = client.patch(url_with_id, data={"name": "test_palette_new"})
    assert resp.status_code == 401
    resp = client.patch(
        url_with_id, data={"name": "test_palette_new"}, headers=headers, content_type='application/json'
    )
    assert resp.status_code == 200

    # retrieve_palette
    resp = client.get(url_with_id)
    assert resp.status_code == 401
    resp = client.get(url_with_id, headers=headers)
    assert resp.status_code == 200
    assert resp.json()['name'] == 'test_palette_new'

    # delete palette
    resp = client.delete(url, data={"id": 1})
    assert resp.status_code == 401
    resp = client.delete(url, data={"id": 1}, headers=headers)
    assert resp.status_code == 405


@pytest.mark.django_db
def test_collors_crud(client: Client, auth_token):
    pass
