from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Location

class LocationSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Location
        geo_field = "point"
        fields = ['id', 'name', 'slug', 'description', 'address', 'city', 
                 'region', 'postal_code', 'created_at']

