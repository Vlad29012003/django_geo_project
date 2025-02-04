from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Review, ReviewImage
from .serializers import ReviewSerializer, ReviewImageSerializer
from django.shortcuts import get_object_or_404


class ReviewAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]


    def get(self, request):
        place = request.query_params.get('place')
        rating = request.query_params.get('rating')
        
        reviews = Review.objects.all()
        if place:
            reviews = reviews.filter(place__slug=place)
        if rating:
            reviews = reviews.filter(rating=rating)
        
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    

    def post(self, request):
        serializer = ReviewSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ReviewDetailAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]


    def get_object(self, pk):
        return get_object_or_404(Review, pk=pk)
    

    def get(self, request, pk):
        review = self.get_object(pk)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    

    def put(self, request, pk):
        review = self.get_object(pk)
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, pk):
        review = self.get_object(pk)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class ReviewLikeAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        review = get_object_or_404(Review, pk=pk)
        if request.user in review.likes.all():
            review.likes.remove(request.user)
            status_msg = 'unliked'
        else:
            review.likes.add(request.user)
            status_msg = 'liked'
        return Response({'status': status_msg})



class ReviewImageUploadAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    parser_classes = [MultiPartParser, FormParser]
    
    def post(self, request, pk):
        review = get_object_or_404(Review, pk=pk)
        serializer = ReviewImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(review=review)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)