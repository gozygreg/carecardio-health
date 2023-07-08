from django.shortcuts import render, get_object_or_404
from .models import Video, VideoSummary


def video_list(request):
    videos = Video.objects.all()
    return render(request, 'academy/video_list.html', {'videos': videos})


def video_detail(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    summary = VideoSummary.objects.get(video=video)
    return render(request, 'academy/video_detail.html', {'video': video, 'summary': summary})
