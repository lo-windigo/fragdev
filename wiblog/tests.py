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

from .models import Post
from images.models import Image
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase


class MarkdownTestCase(TestCase):
    """ Various markdown conversions and formatting
    """

    image_content_type = 'image/gif'
    image_desc = "This is a quick test image"
    image_file = "test.gif"
    image_file_data = b'R0lGODdhAQABAIAAAP///////ywAAAAAAQABAAACAkQBADs='
    image_slug = "test-image"
    image_title = "Test Image"


    def setUp(self):
        test_image = SimpleUploadedFile(self.image_file, self.image_file_data)

        Image.objects.create(title=self.image_title,
                desc=self.image_desc,
                slug=self.image_slug,
                imgFile=test_image,
                content_type=self.image_content_type)
        

    def test_dynamic_image_tag(self):
        """ Test the custom image tag added to support the dynamic image app
        """
        test_image = Image.objects.get(slug=self.image_slug)
        custom_tag = '[I:{}]'.format(self.image_slug)
        resulting_html = '<img src="{}" alt="{}" />'.format(
                    test_image.get_absolute_url(),
                    self.image_desc)
        test_post = Post()

        self.assertEquals(test_post.format_line(custom_tag), resulting_html)

