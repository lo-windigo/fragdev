from django.conf.urls import patterns, url

from fragdev import views

urlpatterns = patterns('',
		    url(r'^$', views.index, name='index')
				)
