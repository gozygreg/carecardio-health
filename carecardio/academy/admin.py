from django.contrib import admin
from django import forms
from .forms import EnrollmentForm
from .models import Course, Module, Quiz, Enrollment
from django.utils.html import escape, strip_tags
from django_summernote.admin import SummernoteModelAdmin
from django_summernote.widgets import SummernoteWidget


class DescriptionAdminMixin(SummernoteModelAdmin):
    summernote_fields = ("description",)  # Fields that will use Summernote

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        return form


class DescriptionWidget(SummernoteWidget):
    def format_value(self, value):
        # Use strip_tags to remove HTML tags and then escape the result
        return escape(strip_tags(value)) if value else ""


@admin.register(Course)
class CourseAdmin(DescriptionAdminMixin):
    list_display = ("title", "short_description")

    def short_description(self, obj):
        return escape(strip_tags(obj.description))


@admin.register(Module)
class ModuleAdmin(DescriptionAdminMixin):
    list_display = ("title", "course", "short_description", "video", "pdf")
    list_filter = ("course",)

    def short_description(self, obj):
        return escape(strip_tags(obj.description))


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ("title", "module")
    list_filter = ("module",)


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ("user", "name", "profession", "course")
    list_filter = ("course", "profession")
    form = EnrollmentForm
