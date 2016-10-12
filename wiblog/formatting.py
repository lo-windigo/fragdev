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

import CommonMark
from images.models import Image
from django.utils.safestring import mark_safe
from django.core.exceptions import ObjectDoesNotExist
import re


def mdToHTML(value):
    """Convert a markdown string into HTML5, and prevent Django from escaping it
    """
    tags = []

    # Find all instance of the dynamic image markdown
    for tag in re.finditer(r'\!\[I:([\w-]+)\]', value):

        tag_slug = tag.group(1)

        try:
            image = Image.objects.get(slug=tag_slug)
            tag_dict = dict()

            tag_dict['start'] = tag.start()
            tag_dict['end'] = tag.end()
            tag_dict['image'] = image

            tags.append(tag_dict)

        except ObjectDoesNotExist:
            pass

    # Replace all of the tags with actual markdown image tags, backwards, to
    # prevent changing string positions and messing up substitution
    for tag_dict in reversed(tags):

        value = value[:tag_dict['start']] + \
            '![{}]({})'.format(tag_dict['image'].desc,
                    tag_dict['image'].get_absolute_url()) + \
            value[tag_dict['end']:]

    return mark_safe(CommonMark.commonmark(value))


def summarize(fullBody):
    """ Get a summary of a post
    """

    firstNewline = fullBody.find("\n")

    if firstNewline > 0:
        return fullBody[:firstNewline]

    return fullBody
