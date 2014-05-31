from django.conf import settings
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('fragdev.views',

		# Blog URLs
    url(r'^blog/', include('wiblog.urls', app_name='wiblog', namespace='wiblog')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

		# Handle all of the "static" pages
		url(r'^$', 'home', name='home'),
		url(r'^about/?$', 'about', name='about'),
		url(r'^about/me/?$', 'aboutMe', name='aboutMe'),
		url(r'^about/skills/?$', 'aboutSkills', name='aboutSkills'),
		url(r'^about/employment/?$', 'aboutEmp', name='aboutEmp'),
		url(r'^about/portfolio/?$', 'aboutPortfolio', name='aboutPortfolio'),
		url(r'^about/education/?$', 'aboutEdu', name='aboutEdu'),
		url(r'^contact/?$', 'contact', name='contact'),
		url(r'^contacted/?$', 'contacted', name='contacted'),
		url(r'^projects/?$', 'projects', name='projects'),
)
