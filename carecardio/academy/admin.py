from django.contrib import admin
from django import forms
from .models import Course, Module, Quiz
from django.utils.html import strip_tags


class DescriptionWidget(forms.Textarea):
    def render(self, name, value, attrs=None, renderer=None):
        value = strip_tags(value) if value else ''
        return super().render(name, value, attrs, renderer)


class DescriptionAdminMixin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if 'description' in form.base_fields:
            form.base_fields['description'].widget = DescriptionWidget()
        return form


@admin.register(Course)
class CourseAdmin(DescriptionAdminMixin):
    list_display = ('title', 'short_description')

    def short_description(self, obj):
        return strip_tags(obj.description)


@admin.register(Module)
class ModuleAdmin(DescriptionAdminMixin):
    list_display = ('title', 'course', 'short_description', 'video')
    list_filter = ('course',)

    def short_description(self, obj):
        return strip_tags(obj.description)


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'module')
    list_filter = ('module',)
