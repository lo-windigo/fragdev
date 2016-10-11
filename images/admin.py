from django.contrib import admin
from .models import Image


class ImageAdmin(admin.ModelAdmin):
    exclude = ('content_type', )
    prepopulated_fields = {'slug': ('title', )}


admin.site.register(Image, ImageAdmin)
