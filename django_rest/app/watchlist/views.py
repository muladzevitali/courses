from django.shortcuts import get_object_or_404
from rest_framework import (mixins, generics, status, viewsets)
from rest_framework.response import Response
from rest_framework.views import APIView

from app.watchlist.models import (WatchList, StreamPlatform, Reviews)
from app.watchlist.serializers import (WatchListSerializer, StreamPlatformSerializer, ReviewSerializer)


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
        serializer = WatchListSerializer(movie)

        return Response(serializer.data)

    def put(self, request, pk):
        movie = get_object_or_404(WatchList, pk=pk)

        serializer = WatchListSerializer(instance=movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        movie = get_object_or_404(WatchList, pk=pk)
        movie.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ReviewDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ReviewListGeneral(generics.ListCreateAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        pk = self.kwargs['movie_id']
        return Reviews.objects.filter(watchlist=pk)


class ReviewDetailGeneral(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer


class ReviewCreate(generics.CreateAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        pk = self.kwargs['movie_id']
        watchlist = get_object_or_404(WatchList, pk=pk)
        serializer.save(watchlist=watchlist)


class StreamPlatformViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(instance=queryset, many=True, context=dict(request=request))

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        stream = get_object_or_404(StreamPlatform, pk=pk)

        serializer = StreamPlatformSerializer(stream, context=dict(request=request))

        return Response(serializer.data)
