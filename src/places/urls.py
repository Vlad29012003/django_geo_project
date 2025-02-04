from django.urls import path
from .views import (
    PlaceAPIView, 
    PlaceDetailAPIView, 
    PlaceImageUploadAPIView
)


urlpatterns = [
    path('places/', PlaceAPIView.as_view(), name='place-list'),
    path('places/<slug:slug>/', PlaceDetailAPIView.as_view(), name='place-detail'),
    path('places/<slug:slug>/images/', PlaceImageUploadAPIView.as_view(), name='place-image-upload'),
]
