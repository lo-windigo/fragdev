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
from wiblog import models


class PostAdmin(admin.ModelAdmin):
    """
    Customize the post admin slightly
    """
    fields = ('title', 'slug', 'body', 'tags', 'status')
    prepopulated_fields = {'slug': ('title', )}


# Register all our models with the built-in admin
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Comment)
admin.site.register(models.Tag)
