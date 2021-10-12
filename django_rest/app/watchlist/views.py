from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import (generics, status, filters)
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from app.watchlist.models import (WatchList, StreamPlatform, Reviews)
from app.watchlist.serializers import (WatchListSerializer, StreamPlatformSerializer, ReviewSerializer)
from . import pagination
from . import throttling
from .permissions import (IsAdminOrReadOnly, IsReviewerOrReadOnly)


class StreamPlatformListApiView(APIView):
    def get(self, request):
        platform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platform, many=True, context=dict(request=request))

        return Response(serializer.data)

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data, context=dict(request=request))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StreamPlatformDetailApiView(APIView):
    def get(self, request, pk):
        platform = get_object_or_404(StreamPlatform, pk=pk)
        serializer = StreamPlatformSerializer(platform, context=dict(request=request))

        return Response(serializer.data)

    def put(self, request, pk):
        platform = get_object_or_404(StreamPlatform, pk=pk)

        serializer = StreamPlatformSerializer(instance=platform, data=request.data, context=dict(request=request))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        platform = get_object_or_404(StreamPlatform, pk=pk)
        platform.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class WatchListApiView(APIView):
    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WatchListDetailApiView(APIView):
    def get(self, request, pk):
        movie = get_object_or_404(WatchList, pk=pk)
        serializer = WatchListSerializer(movie, context=dict(request=self.request))

        return Response(serializer.data)

    def put(self, request, pk):
        movie = get_object_or_404(WatchList, pk=pk)

        serializer = WatchListSerializer(instance=movie, data=request.data, context=dict(request=self.request))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        movie = get_object_or_404(WatchList, pk=pk)
        movie.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class ReviewListGeneral(generics.ListCreateAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer
    throttle_classes = (throttling.ReviewListThrottle,)

    def get_queryset(self):
        pk = self.kwargs['movie_id']
        return Reviews.objects.filter(watchlist=pk)


class ReviewDetailGeneral(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAdminOrReadOnly, IsReviewerOrReadOnly]


class ReviewCreate(generics.CreateAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Reviews.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs['movie_id']
        watchlist = get_object_or_404(WatchList, pk=pk)
        if Reviews.objects.filter(watchlist=pk, user_id=self.request.user.id).exists():
            raise ValidationError('You have already reviewed')

        serializer.save(watchlist=watchlist, user=self.request.user)
        watchlist.average_rating = (watchlist.average_rating * watchlist.number_of_reviews + serializer.validated_data[
            'rating']) / (watchlist.number_of_reviews + 1)
        watchlist.number_of_reviews += 1
        watchlist.save()


class UserReviews(generics.ListAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['user__username', 'is_active']
    search_fields = ('^description',)
    ordering_fields = ('rating',)
    pagination_class = pagination.ReviewPagination
