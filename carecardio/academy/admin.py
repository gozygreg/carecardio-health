from django.contrib import admin
from .models import Video, VideoSummary
from django_summernote.admin import SummernoteModelAdmin
from django_summernote.widgets import SummernoteWidget

# Register your models here.


class VideoAdmin(SummernoteModelAdmin):
    list_display = ('title', 'url',)
    search_fields = ('title',)
    list_filter = ('title',)
    # Add this line to enable Summernote for the 'content' field
    summernote_fields = ('summary',)

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'content':
            formfield.widget = SummernoteWidget(
                attrs={'summernote': {'toolbar': []}})
        return formfield


admin.site.register(VideoSummary)
admin.site.register(Video, VideoAdmin)
