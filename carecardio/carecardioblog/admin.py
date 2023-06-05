from django.contrib import admin
from .models import Category, Post

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    search_fields = ('title', 'category__name')
    list_filter = ('category', 'created_at')


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
