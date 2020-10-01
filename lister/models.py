from django.db import models

# Create your models here.
class VideoDetails(models.Model):
    title = models.CharField('Video Title', max_length=101)
    description = models.TextField(blank=True)
    publishedAt = models.TimeField()
    thumbnailUrl = models.URLField()
    channelName = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class YTApiKey(models.Model):
    apiKey = models.CharField(max_length=55)
    timesUsed = models.IntegerField(default=0)