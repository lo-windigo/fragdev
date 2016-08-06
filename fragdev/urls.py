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
    url(r'^$', views.home, name='home'),
    url(r'^about/?$', views.about, name='about'),
    url(r'^contact/?$', views.contact, name='contact'),
    url(
            r'^contacted/?$',
            TemplateView.as_view(template_name="page-contacted.html"),
            name='contacted'
    ),
    url(
            r'^projects/?$',
            TemplateView.as_view(template_name="page-projects.html"),
            name='projects'
    ),
    url(
            r'^resume/?$',
            TemplateView.as_view(template_name="page-resume.html"),
            name='resume'
    ),
    url(
            r'^hire/?$',
            TemplateView.as_view(template_name="page-hire.html"),
            name='hire'
    ),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
]

# Blog URLs
if 'wiblog' in settings.INSTALLED_APPS:

    import wiblog.urls

    urlpatterns += [
            url(r'^blog/', include(wiblog.urls, app_name='wiblog', namespace='wiblog')),
    ]	
