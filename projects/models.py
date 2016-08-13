from django.db import models


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
    github = models.URLField()
    gitlab = models.URLField()
    website = models.URLField()
    slug = models.SlugField(max_length=150)
