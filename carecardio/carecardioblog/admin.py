from django.contrib import admin
from .models import Category, Post
from django_summernote.admin import SummernoteModelAdmin
from django_summernote.widgets import SummernoteWidget

# Register your models here.


class PostAdmin(SummernoteModelAdmin):
    list_display = ("title", "category", "created_at")
    search_fields = ("title", "category__name")
    list_filter = ("category", "created_at")
    # Add this line to enable Summernote for the 'content' field
    summernote_fields = ("content",)

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == "content":
            formfield.widget = SummernoteWidget(attrs={"summernote": {"toolbar": []}})
        return formfield


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
