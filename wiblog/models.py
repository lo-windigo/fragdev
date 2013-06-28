from django.db import models

# Tag - A text tag, used to categorize posts
class Tag(models.Model):
	desc = models.CharField('Tag', max_length=50)

# Post - a blog post
class Post(models.Model):
	PUBLISH_STATUS = (
			('DFT', 'Draft'),
			('PUB', 'Published'),
	)
	title = models.CharField(max_length=150)
	slug = models.SlugField(max_length=150)
	body = models.TextField()
	tags = models.ManyToManyField(Tag, blank=True)
	status = models.CharField(max_length=150,choices=PUBLISH_STATUS)
	date = models.DateTimeField(auto_now=True)

# Comments - Maybe later.
