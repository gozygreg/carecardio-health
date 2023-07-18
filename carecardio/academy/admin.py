from django.contrib import admin
from .models import Course, Module, Quiz
from django_summernote.admin import SummernoteModelAdmin
from django_summernote.widgets import SummernoteWidget


@admin.register(Course)
class CourseAdmin(SummernoteModelAdmin):
    list_display = ('title', 'description')
    summernote_fields = ('description',)

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'description':
            formfield.widget = SummernoteWidget(
                attrs={'summernote': {'toolbar': []}})
        return formfield


@admin.register(Module)
class ModuleAdmin(SummernoteModelAdmin):
    list_display = ('title', 'course', 'description', 'video')
    list_filter = ('course',)
    summernote_fields = ('description',)

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'description':
            formfield.widget = SummernoteWidget(
                attrs={'summernote': {'toolbar': []}})
        return formfield


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'module')
    list_filter = ('module',)
