from django.conf.urls import patterns, url
#import feeds, views

urlpatterns = patterns('',
	url(r'^archive/$', 'wiblog.views.archive', name='archive'),
	url(r'^archive/(?P<year>\d{4})/$', 'wiblog.views.year', name='year'),
	url(r'^archive/(?P<year>\d{4})/(?P<month>\d{2})/$', 'wiblog.views.month', name='month'),
	url(r'^feeds/atom/$', 'PostFeedAtom()'),
	url(r'^feeds/rss/$', 'PostFeedRSS()'),
	url(r'^tags/$', 'wiblog.views.tags', name='tags'),
	url(r'^tags/(?P<tag>.+)/$', 'wiblog.views.tags', name='tags'),
	url(r'^(?P<slug>.+)$', 'wiblog.views.post', name='post'),
	url(r'^$', 'wiblog.views.index', name='index'),
)
