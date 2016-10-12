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

from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed, Rss201rev2Feed
from wiblog.formatting import mdToHTML
from wiblog.models import Post, Tag


# RSS Feed Class
class PostFeedRSS(Feed):
	feed_type = Rss201rev2Feed
	title = "Jacob Hume - Fragmented Development"
	link = "/blog/feeds/rss"
	description = '''
Jacob Hume's thoughts about web development, technology, Free software and
other miscellaneous topics.
'''

	
	# Get the posts present in this feed
	def items(self):
		# Filter out un-published posts. Should specify tag here as well?
		posts = Post.objects.filter(status='PUB').order_by('-date')

		# Format posts for the feed
		for post in posts:
			post.body = mdToHTML(post.body)

		return posts


	def item_title(self, item):
		# Use the post title for the feed item title
		return item.title


	def item_description(self, item):
		# Use the post body for the feed item "description"
		return item.body


# Atom Feed Class
class PostFeedAtom(PostFeedRSS):
	feed_type = Atom1Feed
	link = "/blog/feeds/atom"
	subtitle = PostFeedRSS.description
