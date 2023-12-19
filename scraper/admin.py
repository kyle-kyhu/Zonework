from django.contrib import admin

from .models import Video


class VideoAdmin(admin.ModelAdmin):
    list_display = (
        'url',
        'title',
        'description',
        'chapters',
    )


admin.site.register(Video, VideoAdmin)