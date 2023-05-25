import pytest
import test_helpers

from django.urls import reverse


pytestmark = [pytest.mark.django_db]


def tests_CustomUser_list_view(client):
    instance1 = test_helpers.create_Account_CustomUser()
    instance2 = test_helpers.create_Account_CustomUser()
    url = reverse("Account_CustomUser_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_CustomUser_create_view(client):
    url = reverse("Account_CustomUser_create")
    data = {
        "email": "user@tempurl.com",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_CustomUser_detail_view(client):
    instance = test_helpers.create_Account_CustomUser()
    url = reverse("Account_CustomUser_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_CustomUser_update_view(client):
    instance = test_helpers.create_Account_CustomUser()
    url = reverse("Account_CustomUser_update", args=[instance.pk, ])
    data = {
        "email": "user@tempurl.com",
    }
    response = client.post(url, data)
    assert response.status_code == 302
