from django.contrib import admin
from .models import Image


class ImageAdmin(admin.ModelAdmin):
    exclude = ('slug', 'content_type')


admin.site.register(Image, ImageAdmin)
