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

from commonmark import commonmark
from django.http import Http404, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.template import loader
from django.utils.safestring import mark_safe
from .models import Project


def index(request):
    '''
    Project listing
    '''

    projects = Project.objects.exclude(status=Project.HIDDEN).order_by('-date')
    template = loader.get_template('projects/page-index.html')

    return HttpResponse(template.render({'projects': projects}))


def project(request, slug):
    '''
    Display project details
    '''

    try:
        project = Project.objects.exclude(status=Project.HIDDEN).get(slug=slug)
    except ObjectDoesNotExist:
        raise Http404('Project "%s" does not exist' % slug)

    # Mark up the markdown in the project description
    project.desc = mark_safe(commonmark(project.desc))   
    
    template = loader.get_template('projects/page-project.html')

    return HttpResponse(template.render({'project': project}))

