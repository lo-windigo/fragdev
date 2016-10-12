# This file is part of the FragDev Website.
# 
# the FragDev Website is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# the FragDev Website is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with the FragDev Website.  If not, see <http://www.gnu.org/licenses/>.

from django.conf import settings
from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.conf.urls.static import static
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

# Set up some custom url patterns for debugging
if settings.DEBUG:
    # Append static files
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    # Append media directory
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Blog URLs
if 'wiblog' in settings.INSTALLED_APPS:

    import wiblog.urls

    urlpatterns += [
            url(r'^blog/', include(wiblog.urls, app_name='wiblog', namespace='wiblog')),
    ]	

if 'images' in settings.INSTALLED_APPS:

    import images.urls

    urlpatterns += [
            url(r'^img/', include(images.urls, app_name='images', namespace='images')),
    ]	
