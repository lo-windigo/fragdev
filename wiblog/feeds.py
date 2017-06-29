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
from . import models


# RSS Feed Class
class PostFeedRSS(Feed):
    feed_type = Rss201rev2Feed
    title = "Jacob Hume - Fragmented Development"
    link = "/blog/feeds/rss"
    description = '''
Jacob Hume's thoughts about web development, technology, Free software and
other miscellaneous topics.
'''
    
    def items(self):
        """
        Get the posts present in this feed
        """
        return  models.Post.published.order_by('-date')

    def item_title(self, item):
        """
        Use the post title for the feed item title
        """
        return item.title


    def item_description(self, item):
        """
        Use the formatted post body for the feed item "description"
        """
        return item.formatted


# Atom Feed Class
class PostFeedAtom(PostFeedRSS):
    feed_type = Atom1Feed
    link = "/blog/feeds/atom"
    subtitle = PostFeedRSS.description

