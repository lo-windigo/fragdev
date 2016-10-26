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


class Project(models.Model):
    '''
    A project that I have contributed to, for display on the Projects page
    '''

    PUBLIC = 'pub'
    HIDDEN = 'hid'
    PROJECT_STATUS = (
        (PUBLIC, 'Public'),
        (HIDDEN, 'Hidden'),
    )

    name = models.CharField(max_length=150)
    desc = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=3, choices=PROJECT_STATUS)
    github = models.URLField(blank=True)
    gitlab = models.URLField(blank=True)
    website = models.URLField(blank=True)
    slug = models.SlugField(max_length=150)
    thumbnail = models.ForeignKey('Image', models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("project", args=[self.slug])

