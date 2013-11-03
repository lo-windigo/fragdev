from django.conf.urls import patterns, url
from wiblog import views
from wiblog.feeds import PostFeedAtom, PostFeedRSS

urlpatterns = patterns('',
	url(r'^archive/?$', 'wiblog.views.archive', name='archive'),
	url(r'^archive/(?P<year>\d{4})/$', 'wiblog.views.year', name='year'),
	url(r'^archive/(?P<year>\d{4})/(?P<month>\d{2})/$', 'wiblog.views.month', name='month'),
	url(r'^feeds/atom/?$', PostFeedAtom(), name='rss'),
	url(r'^feeds/rss/?$', PostFeedRSS(), name='atom'),
	url(r'^tags/?$', 'wiblog.views.tags', name='tags'),
	url(r'^tags/(?P<tag>.+)/$', 'wiblog.views.tags', name='tag'),
	url(r'^(?P<slug>.+)$', 'wiblog.views.post', name='post'),
	url(r'^$', 'wiblog.views.index', name='index'),
)
