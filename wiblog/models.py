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
from django.core.urlresolvers import reverse
from . import managers


class Tag(models.Model):
    """
    A category of post or other object
    """
    desc = models.CharField('Tag', max_length=50, unique=True)

    def __str__(self):
        return self.desc

    def get_absolute_url(self):
        return reverse("wiblog:tags", args=[self.desc])


class Post(models.Model):
    """
    A single blog post
    """
    DFT = 'DFT'
    PUB = 'PUB'
    PUBLISH_STATUS = (
        (DFT, 'Draft'),
        (PUB, 'Published'),
    )
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=150)
    status = models.CharField(max_length=9,
            choices=PUBLISH_STATUS)
    tags = models.ManyToManyField(Tag,
            blank=True,
            null=True)
    title = models.CharField(max_length=150)
    published = managers.PublishedPostManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("wiblog:post", args=[self.slug])


class Comment(models.Model):
    """
    Comments - Other people's input on posts
    """
    HAM = 'HAM'
    SPM = 'SPM'
    UNK = 'UNK'
    MOD_STATUS = (
        (HAM, 'Valid'),
        (SPM, 'Invalid (Spam)'),
        (UNK, 'Unmoderated'),
    )
    comment = models.TextField()
    name = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    moderated = models.CharField(choices=MOD_STATUS,
            default=UNK,
            max_length=14)
    post = models.ForeignKey(Post)
    url = models.URLField(blank=True,
            null=True)

    def __str__(self):
        """
        Provide a decent representation for the admin section
        """
        return '{}: {}'.format(self.name, preview[:75])

