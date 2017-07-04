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

from django.conf.urls import url
from django.views.generic import TemplateView
from wiblog import feeds, views

urlpatterns = [
	url(r'^archive/?$',
            views.ArchiveView.as_view(),
            name='archive'),
	url(r'^comment/?$',
            views.CommentView.as_view(),
            name='comment'),
	url(r'^comment-successful/?$',
            TemplateView.as_view(template_name="page-commented.html"),
            name='comment-successful'),
	url(r'^feeds/atom/?$',
            feeds.PostFeedAtom(),
            name='atom'),
	url(r'^feeds/rss/?$',
            feeds.PostFeedRSS(),
            name='rss'),
	url(r'^tagged/(?P<tag>.+)/$',
            views.TaggedPostView.as_view(),
            name='tagged'),
	url(r'^tags/?$',
            views.TagsView.as_view(),
            name='tags'),
	url(r'^(?P<slug>.+)$',
            views.PostView.as_view(),
            name='post'),
	url(r'^$',
            views.IndexView.as_view(),
            name='index'),
]
