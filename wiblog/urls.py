from django.conf.urls import patterns, url
from wiblog import views
from wiblog.feeds import PostFeedAtom, PostFeedRSS

urlpatterns = patterns('wiblog.views',
	url(r'^archive/?$', 'archive', name='archive'),
	#url(r'^archive/(?P<year>\d{4})/$', 'archive', name='year'),
	url(r'^feeds/atom/?$', PostFeedAtom(), name='rss'),
	url(r'^feeds/rss/?$', PostFeedRSS(), name='atom'),
	url(r'^tags/?$', 'tags', name='tags'),
	url(r'^tags/(?P<tag>.+)/$', 'tags', name='tag'),
	url(r'^(?P<slug>.+)$', 'post', name='post'),
	url(r'^$', 'index', name='index'),
)
