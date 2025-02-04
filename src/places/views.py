from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Place, PlaceImage
from .serializers import PlaceSerializer, PlaceImageSerializer
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication


class PlaceAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    parser_classes = [MultiPartParser, FormParser]


    def get(self, request):
        category = request.query_params.get('category')
        status_filter = request.query_params.get('status')

        places = Place.objects.all()
        if category:
            places = places.filter(category__slug=category)
        if status_filter:
            places = places.filter(status=status_filter)

        serializer = PlaceSerializer(places, many=True)
        return Response(serializer.data)
    

    def post(self, request):
        serializer = PlaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class PlaceDetailAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    parser_classes = [MultiPartParser, FormParser]


    def get_object(self, slug):
        return get_object_or_404(Place, slug=slug)


    def get(self, request, slug):
        place = self.get_object(slug)
        serializer = PlaceSerializer(place)
        return Response(serializer.data)


    def put(self, request, slug):
        place = self.get_object(slug)
        serializer = PlaceSerializer(place, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, slug):
        place = self.get_object(slug)
        place.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class PlaceImageUploadAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    parser_classes = [MultiPartParser, FormParser]


    def post(self, request, slug):
        place = get_object_or_404(Place, slug=slug)
        serializer = PlaceImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(place=place)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
