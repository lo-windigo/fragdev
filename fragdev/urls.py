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
from fragdev import views

# Register admin pages
admin.autodiscover()

urlpatterns = [
    url(r'^$',
        views.HomeView.as_view(),
        name='home'),
    url(r'^about/?$',
        views.AboutView.as_view(),
        name='about'),
    url(r'^contact/?$',
        views.ContactView.as_view(),
        name='contact'),
    url(r'^contacted/?$',
        TemplateView.as_view(template_name="page-contacted.html"),
        name='contacted'
    ),
    url(r'^contacted/?$',
        TemplateView.as_view(template_name="page-contacted.html"),
        name='contacted'
    ),
    url(r'^mei2019/?$',
        TemplateView.as_view(template_name="page-mei2019.html"),
        name='mei2019'
    ),
    url(r'^minecraft/?$',
        TemplateView.as_view(template_name="page-minecraft.html"),
        name='minecraft'
    ),
    url(r'^resume/?$',
        TemplateView.as_view(template_name="page-resume.html"),
        name='resume'
    ),
#    url(r'^hire/?$',
#        TemplateView.as_view(template_name="page-hire.html"),
#        name='hire'
#    ),
    url(r'^admin/', admin.site.urls),
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
        url(r'^blog/', include(wiblog.urls)),
    ]	


# Dynamic image URLs
if 'images' in settings.INSTALLED_APPS:

    import images.urls

    urlpatterns += [
        url(r'^img/', include(images.urls)),
    ]	


# Project URLs
if 'projects' in settings.INSTALLED_APPS:

    import projects.urls

    urlpatterns += [
        url(r'^projects/', include(projects.urls)),
    ]	

