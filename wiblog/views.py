# Create your views here.
from django.http import HttpResponse
from django.template import Context, RequestContext, loader
from wiblog.models import Post, Tag


# Blog Index
def index(request):

	template = loader.get_template('base-index.html')

	# Get a few posts to start with
	# TODO: Figure out how to reference the choices, instead of hard-coding!
	posts = Post.objects.filter(status='PUB').order_by('date')[:5]

	context = Context({'posts': posts})
	return HttpResponse(template.render(context))


# Archive page
def archive(request):

	template = loader.get_template('base-archive.html')

	# Get all posts
	posts = Post.objects.filter(status='PUB').order_by('date')

	context = Context({'posts': posts})
	return HttpResponse(template.render(context))


# Feeds
def feeds(request):

	template = loader.get_template('base-feeds.html')

	context = Context({'feeds': feeds})
	return HttpResponse(template.render(context))


# A single blog post
def post(request, slug):

	template = loader.get_template('base-post.html')

	post = Post.objects.get(slug=slug)

	context = Context({'post': post})
	return HttpResponse(template.render(context))


# Tags Tags TAGS
def tags(request):

	template = loader.get_template('base-tags.html')
	
	# Get any tags that have been defined
	tags = Tag.objects.all()

	context = Context({'tags': tags})
	return HttpResponse(template.render(context))
