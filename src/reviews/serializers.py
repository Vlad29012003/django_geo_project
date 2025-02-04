from rest_framework import serializers
from .models import Review, ReviewImage


class ReviewImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewImage
        fields = ['id', 'image', 'created_at']


class ReviewSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)
    images = ReviewImageSerializer(many=True, read_only=True)
    likes_count = serializers.IntegerField(source='likes.count', read_only=True)


    class Meta:
        model = Review
        fields = ['id', 'place', 'user', 'user_name', 'rating', 'title', 
                 'comment', 'visit_date', 'likes_count', 'is_verified', 
                 'images', 'created_at']
        read_only_fields = ['user', 'is_verified', 'likes_count']