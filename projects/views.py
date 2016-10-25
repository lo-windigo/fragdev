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

from django.http import Http404
from django.shortcuts import render
from django.template import loader
from models import Project


def index(request):
    '''
    Project listing
    '''

    projects = Project.objects.filter(status=Project.PUBLIC).order_by('-date')
    template = loader.get_template('projects/page-index.html')

    return HttpResponse(template.render({'projects': projects}))


def project(request, slug):
    '''
    Display project details
    '''

    try:
        project = Project.objects.get(slug=slug,status=Project.PUBLIC)
    except ObjectDoesNotExist:
        raise Http404('Project {} does not exist' % slug)

    template = loader.get_template('projects/page-project.html')

    return HttpResponse(template.render({'project': project}))

