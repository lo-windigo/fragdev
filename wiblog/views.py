# Create your views here.
from django.http import HttpResponse
from django.template import Context, RequestContext, loader
from wiblog.formatting import mdToHTML, summarize
from wiblog.models import Post, Tag


# Blog Index
def index(request):

	template = loader.get_template('base-wiblog.html')

	# Get a few posts to start with
	# TODO: Figure out how to reference choices, instead of hard-coding!
	posts = Post.objects.filter(status='PUB').order_by('date')[:5]

	# Go through all the posts, trim and format the post body
	for post in posts:

		post.body = mdToHTML(summarize(post.body))

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
	
	context = Context({'posts': orderedPosts})
	return HttpResponse(template.render(context))


# A single blog post
def post(request, slug):

	template = loader.get_template('base-post.html')

	post = Post.objects.get(slug=slug)

	post.body = mdToHTML(post.body)

	context = Context({'post': post})
	return HttpResponse(template.render(context))


# Tags Tags TAGS
def tags(request):

	template = loader.get_template('base-tags.html')
	
	# Get any tags that have been defined
	tags = Tag.objects.order_by('desc')

	context = Context({'tags': tags})
	return HttpResponse(template.render(context))


# Tagged Posts
def tagged_posts(request, tag):

	template = loader.get_template('base-tagged.html')

	tagObj = Tag.objects.get(desc=tag)

	# Get the tag we're looking for
	posts = Post.objects.get(tags=tagObj)

	# Get all posts
	#posts = tag.post_set.all().order_by('-date')

	context = Context({'posts': posts})
	return HttpResponse(template.render(context))
