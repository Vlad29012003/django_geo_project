from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Location
from .serializers import LocationSerializer
from django.shortcuts import get_object_or_404


class LocationAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]


    def get(self, request):
        city = request.query_params.get('city')
        region = request.query_params.get('region')
        
        locations = Location.objects.all()
        if city:
            locations = locations.filter(city__icontains=city)
        if region:
            locations = locations.filter(region__icontains=region)
        
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)
    

    def post(self, request):
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LocationDetailAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]


    def get_object(self, slug):
        return get_object_or_404(Location, slug=slug)


    def get(self, request, slug):
        location = self.get_object(slug)
        serializer = LocationSerializer(location)
        return Response(serializer.data)
    

    def put(self, request, slug):
        location = self.get_object(slug)
        serializer = LocationSerializer(location, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, slug):
        location = self.get_object(slug)
        location.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
