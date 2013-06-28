from django.conf import settings
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
		# Blog URLs
    #url(r'^blog/(?P<path>.*)', include('wiblog.urls', namespace='wiblog')),

		# Handle all of the "static" pages
		url(r'^$', 'fragdev.views.home', name='home'),
		url(r'^about$', 'fragdev.views.about', name='about'),
		url(r'^contact$', 'fragdev.views.contact', name='contact'),
		url(r'^contacted$', 'fragdev.views.contacted', name='contacted'),
		url(r'^projects$', 'fragdev.views.projects', name='projects'),
		url(r'^resume$', 'fragdev.views.resume', name='resume'),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

		# if settings.DEBUG:
		# DEBUGGING: Static media paths
		url(r'^css/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': '/data/documents/web/fragdev4000/css'}),
		url(r'^fonts/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': '/data/documents/web/fragdev4000/fonts'}),
)
