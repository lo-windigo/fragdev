from django.conf.urls import patterns, url
from wiblog import views
from wiblog.feeds import PostFeedAtom, PostFeedRSS

urlpatterns = patterns('wiblog.views',
	url(r'^archive/?$', 'archive', name='archive'),
	url(r'^feeds/atom/?$', PostFeedAtom(), name='rss'),
	url(r'^feeds/rss/?$', PostFeedRSS(), name='atom'),
	url(r'^tagged/(?P<tag>.+)/$', 'tagged_posts', name='tagged'),
	url(r'^tags/?$', 'tags', name='tags'),
	url(r'^(?P<slug>.+)$', 'post', name='post'),
	url(r'^$', 'index', name='index'),
)
