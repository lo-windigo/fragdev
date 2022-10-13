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

from django.urls import path 
from django.views.generic import TemplateView
from wiblog import feeds, views

app_name = 'wiblog'

urlpatterns = [
	path('archive/',
            views.ArchiveView.as_view(),
            name='archive'),
	path('comment/',
            views.CommentView.as_view(),
            name='comment'),
	path('comment-successful/',
            TemplateView.as_view(template_name="page-commented.html"),
            name='comment-successful'),
	path('feeds/atom/',
            feeds.PostFeedAtom(),
            name='atom'),
	path('feeds/rss/',
            feeds.PostFeedRSS(),
            name='rss'),
	path('tagged/<tag>/',
            views.TaggedPostView.as_view(),
            name='tagged'),
	path('tags/',
            views.TagsView.as_view(),
            name='tags'),
	path('<slug>',
            views.PostView.as_view(),
            name='post'),
	path('',
            views.IndexView.as_view(),
            name='index'),
]
