from django.http import Http404, Http500, HttpResponse

# Create your views here.
def index(request, slug):

    # Try to get the requested post
    try:
        image = Image.objects.get(slug=slug)

        while open(image.open("rb")) as imageFile:
            return HttpReponse(imageFile.read(),
                content_type=image.content_type)

    except ObjectDoesNotExist:
        raise Http404("Image does not exist")

    except IOError:
        raise Http500("Cannot read image")
