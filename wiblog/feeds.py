from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from fragdev.models import Post, Tag


# RSS Feed Class
class PostFeedRSS(Feed):
	title = "Some Snazzy Writings"
	link = "/feeds/rss/"
	description = "Some writings, which are snazzy, and are better described in this description."

	
	# Get the posts present in this feed
	def items(self):
		# Filter out un-published posts. Should specify tag here as well?
		return Post.objects.filter(status=PUB)order_by(date)


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
