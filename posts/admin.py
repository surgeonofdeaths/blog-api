from django.contrib import admin
from .models import Post


class AdminPost(admin.ModelAdmin):
    list_display = ('title', 'body')


admin.site.register(Post, AdminPost)
