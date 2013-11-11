# Create your views here.
from django.http import HttpResponse
from django.template import Context, RequestContext, loader
from django.utils.safestring import mark_safe
import markdown
from wiblog.models import Post, Tag


# Blog Index
def index(request):

	template = loader.get_template('base-index.html')

	# Get a few posts to start with
	# TODO: Figure out how to reference choices, instead of hard-coding!
	posts = Post.objects.filter(status='PUB').order_by('date')[:5]

	# Go through all the posts, trim and format the post body
	for post in posts:

		firstNewline = post.body.find("\n")

		if firstNewline > 0:
			post.body = str(post.body)[:firstNewline]

		post.body = mdToHTML(post.body)

	context = Context({'posts': posts})
	return HttpResponse(template.render(context))


# Archive page
def archive(request):

	template = loader.get_template('base-archive.html')

	# Get all posts
	posts = Post.objects.filter(status='PUB').order_by('date')
	orderedPosts = {}

	# Go through all the posts and sort them by year
	for post in posts:
		
		year = post.date.year
		
		# If this is the first post of the year, start a new list
		if year not in orderedPosts:
			orderedPosts[year] = []

		orderedPosts[year].append(post)
	
	context = Context({'posts': orderedPosts, 'current_app': 'wiblog'})
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

	post.body = mdToHTML(post.body)
	post.tags = post.tags.items

	context = Context({'post': post})
	return HttpResponse(template.render(context))


# Tags Tags TAGS
def tags(request):

	template = loader.get_template('base-tags.html')
	
	# Get any tags that have been defined
	tags = Tag.objects.all()

	context = Context({'tags': tags})
	return HttpResponse(template.render(context))


## Helper Functions ##

def mdToHTML(value):
	return mark_safe(markdown.markdown(value, output_format="html5"))
