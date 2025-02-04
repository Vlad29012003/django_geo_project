from rest_framework import serializers
from .models import Place, PlaceImage
from locations.serializers import LocationSerializer


class PlaceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceImage
        fields = ['id', 'image', 'description', 'is_main', 'created_at']


class PlaceSerializer(serializers.ModelSerializer):
    images = PlaceImageSerializer(many=True, read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)
    location_details = LocationSerializer(source='location', read_only=True)
    average_rating = serializers.FloatField(read_only=True)

    class Meta:
        model = Place
        fields = ['id', 'name', 'slug', 'description', 'category', 'category_name',
                 'location', 'location_details', 'status', 'rating', 'phone', 
                 'website', 'email', 'main_image', 'working_hours', 'price_level',
                 'features', 'images', 'average_rating', 'created_at']
