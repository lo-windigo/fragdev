from django.contrib import admin
from wiblog.models import Comment,Post,Tag

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Comment)
