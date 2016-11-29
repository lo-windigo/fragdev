# This file is part of the FragDev Website.
# 
# the FragDev Website is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# the FragDev Website is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with the FragDev Website.  If not, see <http://www.gnu.org/licenses/>.

from django.contrib import admin
from wiblog.models import Comment,Post,Tag


class PostAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'body', 'tags', 'status')
    prepopulated_fields = {'slug': ('title', )}


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment)
