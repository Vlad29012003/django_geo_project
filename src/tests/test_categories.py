import pytest
from django.urls import reverse
from rest_framework import status
from tests.factories import CategoryFactory
from categories.models import Category



@pytest.mark.django_db
class TestCategoryAPI:
    
    def test_get_categories(self, api_client):
        CategoryFactory.create_batch(3)  
        url = reverse("category-list")
        response = api_client.get(url)
        
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 3


    def test_create_category_unauthorized(self, api_client):
        url = reverse("category-list")
        data = {"name": "New Category", "slug": "new-category"}
        response = api_client.post(url, data)
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED


    def test_create_category_authorized(self, auth_client):
        url = reverse("category-list")
        data = {"name": "New Category", "slug": "new-category"}
        response = auth_client.post(url, data)
        
        assert response.status_code == status.HTTP_201_CREATED
        assert Category.objects.count() == 1


    def test_get_category_detail(self, api_client):
        category = CategoryFactory()
        url = reverse("category-detail", kwargs={"slug": category.slug})
        response = api_client.get(url)
        
        assert response.status_code == status.HTTP_200_OK
        assert response.data["name"] == category.name


    def test_update_category_unauthorized(self, api_client):
        category = CategoryFactory()
        url = reverse("category-detail", kwargs={"slug": category.slug})
        data = {"name": "Updated Name", "slug": category.slug}
        response = api_client.put(url, data)
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED


    def test_update_category_authorized(self, auth_client):
        category = CategoryFactory()
        url = reverse("category-detail", kwargs={"slug": category.slug})
        data = {"name": "Updated Name", "slug": category.slug}
        response = auth_client.put(url, data)
        
        assert response.status_code == status.HTTP_200_OK
        category.refresh_from_db()
        assert category.name == "Updated Name"


    def test_delete_category_unauthorized(self, api_client):
        category = CategoryFactory()
        url = reverse("category-detail", kwargs={"slug": category.slug})
        response = api_client.delete(url)

        assert response.status_code == status.HTTP_401_UNAUTHORIZED



    def test_delete_category_authorized(self, auth_client):
        category = CategoryFactory()
        url = reverse("category-detail", kwargs={"slug": category.slug})
        response = auth_client.delete(url)
        
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Category.objects.count() == 0