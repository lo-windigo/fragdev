#
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

from django.db import models
from wiblog import models as w_models


class ApprovedCommentsManager(models.Manager):
    """
    A manager that filters out unmoderated comments
    """
    def get_queryset(self):
        return super().get_queryset().filter(moderated=w_models.Comment.HAM)


class PublishedPostManager(models.Manager):
    """
    A manager that only deals with published posts
    """
    def get_queryset(self):
        return super().get_queryset().filter(status=w_models.Post.PUB)

