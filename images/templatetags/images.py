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

from django import template
from django.utils.html import format_html
from images.models import Image

register = template.Library()


@register.simple_tag
def image(arg):
    """
    Get an image tag for an Image model (based on slug)
    """
    try:
        image_model = Image.objects.get(slug=arg)

        return format_html(
		    '<img src="{}" alt="{}">',
		    image_model.get_absolute_url(),
		    image_model.desc
		)

    except:
        return format_html(
                    '<!-- Cannot retrieve image: {} -->',
                    arg
                )

@register.simple_tag
def image_thumbnail(arg):
    """
    Get a thumbnail image & anchor for an Image model (based on slug)
    """
    try:
        image_model = Image.objects.get(slug=arg)

        return format_html(
		    '<a href="{url}"><img src="{url}" alt="{desc}"></a>',
		    url=image_model.get_absolute_url(),
		    desc=image_model.desc
		)

    except:
        return format_html(
                    '<!-- Cannot retrieve image: {} -->',
                    arg
                )

