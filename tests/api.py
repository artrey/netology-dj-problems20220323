import pytest
from rest_framework.test import APIClient

from demo.models import Order





@pytest.mark.django_db
def test_create_product():
    client = APIClient()
    order = Order.objects.create()
    response = client.post('/products/', data={
        "name": "New product",
        "price": 1000,
        "positions": [
            {
                "order": order.id,
                "qty": 22
            }
        ]
    }, format='json')
    assert response.status_code == 201


@pytest.mark.django_db
def test_create_product():
    client = APIClient()
    order = Order.objects.create()
    response = client.patch('/products/', data={
        "name": "New product",
        "price": 1000,
        "positions": [
            {
                "order": order.id,
                "qty": 22
            }
        ]
    }, format='json')
    assert response.status_code == 201
