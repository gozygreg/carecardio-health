from django import forms
from .models import Video, VideoSummary


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'summary',)
