from django.db import models
from django.core.urlresolvers import reverse


class Project(models.Model):
    '''
    A open source/development project to be displayed on the Projects page
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

    def __str__(self):
            return self.name

    def get_absolute_url(self):
        return reverse("project", args=[self.project])
