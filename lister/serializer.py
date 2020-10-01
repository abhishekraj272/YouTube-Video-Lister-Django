from rest_framework import serializers
from .models import VideoDetails


class VideoDetailSerializers(serializers.ModelSerializer):

    class Meta:
        model = VideoDetails
        fields = ('videoId', 'title', 'description', 'publishedAt', 'thumbnailUrl', 'channelName')