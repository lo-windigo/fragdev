from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from django.utils.feedgenerator import Atom1Feed, Rss201rev2Feed
from wiblog.formatting import mdToHTML, summarize
from wiblog.models import Post, Tag


# RSS Feed Class
class PostFeedRSS(Feed):
	feed_type = Rss201rev2Feed
	title = "Jacob Hume - Fragmented Development"
	link = "/feeds/rss"
	description = '''
Jacob Hume's thoughts about web development, technology, Free software and
other miscellaneous topics.
'''

	
	# Get the posts present in this feed
	def items(self):
		# Filter out un-published posts. Should specify tag here as well?
		posts = Post.objects.filter(status='PUB').order_by('date')

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
	subtitle = PostFeedRSS.description
