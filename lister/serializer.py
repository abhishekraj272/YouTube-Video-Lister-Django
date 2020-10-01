from rest_framework import serializers
from .models import VideoDetails


class VideoDetailSerializers(serializers.ModelSerializer):

    class Meta:
        model = VideoDetails
        fields = ('title', 'description', 'publishedAt', 'thumbnailUrl', 'channelName')