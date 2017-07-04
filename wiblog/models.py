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

import re
from CommonMark import commonmark
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.safestring import mark_safe
from wiblog import choices, managers
from images.models import Image


class Tag(models.Model):
    """
    A category of post or other object
    """
    desc = models.SlugField('Tag', max_length=50, unique=True)

    def __str__(self):
        return self.desc

    def get_absolute_url(self):
        return reverse("wiblog:tags", args=[self.desc])


class Post(models.Model):
    """
    A single blog post
    """
    DFT = choices.PostChoices.DFT
    PUB = choices.PostChoices.PUB
    PUBLISH_STATUS = choices.PostChoices.PUBLISH_STATUS
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=150)
    status = models.CharField(max_length=9,
            choices=PUBLISH_STATUS)
    tags = models.ManyToManyField(Tag,
            blank=True)
    title = models.CharField(max_length=150)

    # Define model managers
    objects = models.Manager() 
    published = managers.PublishedPostManager()

    def __str__(self):
        """
        Use the post title to represent the object in the admin section
        """
        return self.title

    def get_absolute_url(self):
        """
        Use the post title to represent the object in the admin section
        """
        return reverse("wiblog:post", args=[self.slug])

    def format(self, markdown):
        """
        Format markdown into HTML, including custom image tags
        """
        tags = []

        # Find all instance of the dynamic image markdown
        for tag in re.finditer(r'\!\[I:([\w-]+)\]', self.body):

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

            markdown = markdown[:tag_dict['start']] + \
                '![{}]({})'.format(tag_dict['image'].desc,
                        tag_dict['image'].get_absolute_url()) + \
                markdown[tag_dict['end']:]

        return mark_safe(commonmark(markdown))

    @property
    def formatted(self):
        """
        Return the rendered post body
        """
        return self.format(self.body)

    @property
    def formatted_summary(self):
        """
        Return a rendered post summary
        """
        try:
            summary = self.body[:self.body.index("\n")]
        except:
            summary = self.body

        return self.format(summary)


class Comment(models.Model):
    """
    Comments - Other people's input on posts
    """
    HAM = choices.CommentChoices.HAM
    SPM = choices.CommentChoices.SPM
    UNK = choices.CommentChoices.UNK
    MOD_STATUS = choices.CommentChoices.MOD_STATUS
    comment = models.TextField()
    name = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    moderated = models.CharField(choices=MOD_STATUS,
            default=UNK,
            max_length=14)
    post = models.ForeignKey(Post)
    url = models.URLField(blank=True,
            null=True)

    # Define model managers
    objects = models.Manager() 
    approved = managers.ApprovedCommentsManager()

    def __str__(self):
        """
        Provide a decent representation for the admin section
        """
        return '{}: {}'.format(self.name, self.comment[:75])

    def format(self, markdown):
        """
        Format markdown into HTML
        """
        return mark_safe(commonmark(markdown))

    @property
    def formatted(self):
        """
        Return the rendered comment body
        """
        return self.format(self.comment)

