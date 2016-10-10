# This file is part of FragDev.
#
# FragDev is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# FragDev is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with FragDev.  If not, see <http://www.gnu.org/licenses/>.

from django.http import Http404, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import Image


def image(request, slug):
    '''
    Return a single image
    '''

    # Try to get the requested post
    try:
        image = Image.objects.get(slug=slug)
        imageFile = image.imgFile.open("rb")
        return HttpReponse(imageFile.read(),
            content_type="image/{}".format(image.content_type))

    except ObjectDoesNotExist:
        raise Http404("Image does not exist")
