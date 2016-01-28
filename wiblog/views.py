from django.template.context_processors import csrf
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import Context, RequestContext, loader
from wiblog.formatting import mdToHTML, summarize
from wiblog.models import Comment, Post, Tag
from wiblog.comments import CommentForm


## Blog Index
def index(request):

	template = loader.get_template('base-wiblog.html')

	# Get a few posts to start with
	posts = Post.objects.filter(status=Post.PUB).order_by('-date')[:5]

	# Go through all the posts, trim and format the post body
	for post in posts:

		post.body = mdToHTML(post.body)

	context = Context({'posts': posts})
	return HttpResponse(template.render(context))


## Archive page
def archive(request):

	template = loader.get_template('base-archive.html')

	# Get all posts
	posts = Post.objects.filter(status=Post.PUB).order_by('-date')
	orderedPosts = {}

	# Go through all the posts and sort them by year
	for post in posts:
		
		year = post.date.year
		
		# If this is the first post of the year, start a new list
		if year not in orderedPosts:
			orderedPosts[year] = []

		# Append this post to the year list
		orderedPosts[year].append(post)
	
	context = Context({'posts': orderedPosts})
	return HttpResponse(template.render(context))


## A single blog post
def post(request, slug):

	template = loader.get_template('base-post.html')

	# Try to get the requested post
	try:
		post = Post.objects.get(slug=slug)
	except ObjectDoesNotExist:
		return redirect('wiblog:archive')

	# If the form has been submitted...
	if request.method == 'POST':

		# A form bound to the POST data
		comment = Comment(post=post)
		form = CommentForm(request.POST, instance=comment)

		# Form was validated, and contained good data
		if form.is_valid():

			# Save the comment
			form.save()

			# notify a mod
			import smtplib
			from email.mime.text import MIMEText

			sender = 'wiblog@fragdev.com'
			sendee = 'jacob@fragdev.com'
	
			msg = MIMEText('New Comment')
			msg['Subject'] = 'Comments awaiting moderation'
			msg['From'] = sender
			msg['To'] = sendee

			mailServer = smtplib.SMTP('localhost')
			mailServer.sendmail(sender, [sendee], msg.as_string())
			mailServer.quit

	# If the form hasn't been submitted, get a blank form
	else:
		form = CommentForm() 

	# Get any comments that go with a post
	# TODO: Add Pagination if you become wildly popular
	comments = Comment.objects.filter(post=post,moderated=Comment.HAM).order_by('-date')

	# Format the post body for display
	post.body = mdToHTML(post.body)

	# Format the comments for display
	for comment in comments:
		comment.comment = mdToHTML(comment.comment)

	context = RequestContext(request, {'form': form, 'post': post, 'comments': comments})
	return HttpResponse(template.render(context))


## Tags Tags TAGS
def tags(request):

	template = loader.get_template('base-tags.html')
	
	# Get any tags that have been defined
	tags = Tag.objects.order_by('desc')

	context = Context({'tags': tags})
	return HttpResponse(template.render(context))


## Tagged Posts
def tagged_posts(request, tag):

	template = loader.get_template('base-tagged.html')

	# Get the tag we're looking for
	try:
		tagObj = Tag.objects.get(desc=tag)
	except ObjectDoesNotExist:
		return redirect('wiblog:tags')

	# Return any posts that are tagged with this
	posts = Post.objects.filter(tags=tagObj,status=Post.PUB)

	# Go through all the posts, trim and format the post body
	for post in posts:

		post.body = mdToHTML(summarize(post.body))

	context = Context({'posts': posts, 'tag': tagObj})
	return HttpResponse(template.render(context))
