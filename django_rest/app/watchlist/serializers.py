from rest_framework import serializers

from .models import (WatchList, StreamPlatform, Reviews)


class ReviewSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='watchlist:review_detail')

    class Meta:
        model = Reviews
        fields = '__all__'


class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = WatchList
        fields = '__all__'
        read_only_fields = ['id', ]
        validators = (serializers.UniqueTogetherValidator(
            queryset=WatchList.objects.all(),
            fields=['title', 'storyline']
        ),)

    def validate_name(self, value):
        if 'invalid' in value:
            raise serializers.ValidationError('Invalid name')

        return value

    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Name and description mustn't be same")

        return data


class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="watchlist:stream_detail")
    watchlist = serializers.HyperlinkedIdentityField(many=True, view_name='watchlist:movie_detail')

    class Meta:
        model = StreamPlatform
        fields = '__all__'
        validators = (serializers.UniqueTogetherValidator(
            queryset=StreamPlatform.objects.all(),
            fields=['name', 'website']
        ),)
