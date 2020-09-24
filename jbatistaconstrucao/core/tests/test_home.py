from django.test import Client
import pytest


@pytest.mark.django_db
def test_status_code(client: Client):
    resp = client.get('/')
    assert resp.status_code == 200
