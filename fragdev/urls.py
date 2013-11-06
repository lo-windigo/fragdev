from django.conf import settings
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('fragdev.views',

		# Blog URLs
    url(r'^blog/', include('wiblog.urls', app_name='wiblog', namespace='wiblog')),

		# Handle all of the "static" pages
		url(r'^$', 'home', name='home'),
		url(r'^about$', 'about', name='about'),
		url(r'^contact$', 'contact', name='contact'),
		url(r'^contacted$', 'contacted', name='contacted'),
		url(r'^projects$', 'projects', name='projects'),
		url(r'^resume$', 'resume', name='resume'),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
