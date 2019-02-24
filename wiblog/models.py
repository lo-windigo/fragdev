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
from commonmark import commonmark
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from django.utils.timezone import now
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
    date = models.DateTimeField(default=now)
    updated = models.DateTimeField(blank=True, null=True)
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
        for tag in re.finditer(r'\[I:([\w-]+)\]', markdown):

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


    def format_line(self, markdown):
        """
        Renders a single line of markdown as HTML without inserting it into a
        paragraph tag
        """
        html = self.format(markdown)

        if html.startswith('<p>'):
            html = html[3:]

        if html.endswith('</p>\n'):
            html = html[:-5]

        return mark_safe(html)


    def comments(self):
        """
        Only return moderated comments that apply to this post
        """
        return Comment.approved.filter(post=self.pk)


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

        # FIX: For some reason, CRLF line endings are getting into Post data??
        post_text = self.body.replace("\r", "")

        # Get the first paragraph of text, and format that
        try:
            summary = post_text[:post_text.index("\n\n")]
        except ValueError:
            summary = post_text

        return self.format(summary)


    @property
    def formatted_title(self):
        """
        Return the rendered post body
        """
        return self.format_line(self.title)


    def save(self, show_updated=True):
        """
        Override the save method to do a bunch of sensible stuff, like setting
        default field values and setting up the slug field
        """

        # Default slug: just slugify the title
        if not self.slug:
            self.slug = slugify(self.title)

        # Update the updated time, if this is an existing object
        if self.id and show_updated:
            self.updated = now()

        # Call the actual save method
        super().save()


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
    post = models.ForeignKey(Post, models.CASCADE)
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

