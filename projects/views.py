from django.shortcuts import render
from models import project

def index(request):
    '''
    Project listing
    '''

    projects = Project.objects.filter(status=Project.PUBLIC).order_by('-date')


    return HttpResponse(template.render({'projects': projects}))


def project(request, slug):
    '''
    Display project details
    '''

    try:
        project = Project.objects.get(slug=slug)
    except ObjectDoesNotExist:

        #TODO: Maybe a better option, like 404?
        pass
        #return redirect('')

    return HttpResponse(template.render({'projects': projects}))
