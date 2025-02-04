from django.urls import path
from .views import LocationAPIView, LocationDetailAPIView

urlpatterns = [
    path('locations/', LocationAPIView.as_view(), name='location-list'),
    path('locations/<slug:slug>/', LocationDetailAPIView.as_view(), name='location-detail'),
]