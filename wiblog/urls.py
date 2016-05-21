from django.conf.urls import patterns, url
from wiblog import views
from wiblog.feeds import PostFeedAtom, PostFeedRSS

urlpatterns = [
	url(r'^archive/?$', views.archive, name='archive'),
	url(r'^feeds/atom/?$', PostFeedAtom(), name='atom'),
	url(r'^feeds/rss/?$', PostFeedRSS(), name='rss'),
	url(r'^tagged/(?P<tag>.+)/$', views.tagged_posts, name='tagged'),
	url(r'^tags/?$', views.tags, name='tags'),
	url(r'^(?P<slug>.+)$', views.post, name='post'),
	url(r'^$', views.index, name='index'),
]
