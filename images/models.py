from django.db import models
from django.utils.text import slugify


class Image(models.Model):
    '''
    Represents a single uploaded image
    '''
    desc = models.CharField(max_length=250)
    date = models.DateTimeFiel(auto_now_add=True)
    imgFile = models.FileField(upload_to='img/')
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):

        if not self.id and self.slug is None:
            self.slug = slugify(self.desc)

        super(Image, self).save(*args, *kwargs)
