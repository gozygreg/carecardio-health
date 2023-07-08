from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()


class VideoSummary(models.Model):
    video = models.OneToOneField(Video, on_delete=models.CASCADE)
    summary = models.TextField()
