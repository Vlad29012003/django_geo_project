from django.urls import path
from .views import (
    ReviewAPIView, 
    ReviewDetailAPIView, 
    ReviewLikeAPIView, 
    ReviewImageUploadAPIView
)


urlpatterns = [
    path('reviews/', ReviewAPIView.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewDetailAPIView.as_view(), name='review-detail'),
    path('reviews/<int:pk>/like/', ReviewLikeAPIView.as_view(), name='review-like'),
    path('reviews/<int:pk>/images/', ReviewImageUploadAPIView.as_view(), name='review-image-upload'),
]
