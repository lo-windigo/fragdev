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


## Tag - A text tag, used to categorize posts
class Tag(models.Model):
	desc = models.CharField('Tag', max_length=50, unique=True)

	def __str__(self):
		return self.desc

	def get_absolute_url(self):
		return reverse("wiblog:tags", args=[self.desc])


## Post - a blog post
class Post(models.Model):
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
	status = models.CharField(max_length=9, choices=PUBLISH_STATUS)
	tags = models.ManyToManyField(Tag, blank=True)
	title = models.CharField(max_length=150)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("wiblog:post", args=[self.slug])


## Comments - Other people's input on posts
class Comment(models.Model):
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
	moderated = models.CharField(choices=MOD_STATUS, default=UNK, max_length=14)
	post = models.ForeignKey(Post)
	url = models.URLField()


	# Provide a decent representation for the admin section
	def __str__(self):

		prev = self.comment

		if len(prev) > 75:
			prev = prev[0:75]+"..."

		return "'"+self.name+"' Says: '"+prev+"'"
