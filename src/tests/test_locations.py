import pytest
from django.urls import reverse
from rest_framework import status
from .factories import LocationFactory



@pytest.mark.django_db
class TestLocationAPI:
    def test_get_location_list(self, api_client):
        LocationFactory.create_batch(2)
        url = reverse("location-list")
        response = api_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2


    def test_get_location_detail(self, api_client):
        location = LocationFactory()
        url = reverse("location-detail", kwargs={"slug": location.slug})
        response = api_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data["id"] == location.id




    
