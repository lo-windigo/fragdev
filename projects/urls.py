from django.conf import settings
from django.conf.urls import include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# Include any views
from . import views


urlpatterns = [

    # Handle all of the "static" pages
    url(r'^$', views.home, name='projects'),
    url(r'^(?P<slug>.+)$', views.post, name='post'),
]

# Blog URLs
if 'projects' in settings.INSTALLED_APPS:

    urlpatterns += [
            url(r'^projects/', include(projects.urls, app_name='projects',
                namespace='projects')),
    ]	
