from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, RequestContext, loader
from django.template.context_processors import csrf
from django.core.urlresolvers import reverse
from fragdev.contact import ContactForm
import time


def home(request):
	template = loader.get_template('page-home.html')
	post = False

	# Try to get the latest blog post
	if 'wiblog' in settings.INSTALLED_APPS:
		from wiblog.models import Post
		from wiblog.formatting import mdToHTML, summarize

		if Post.objects.count() > 0:
			post = Post.objects.filter(status=Post.PUB).order_by('-date')[0]
			post.body = mdToHTML(summarize(post.body))

	return HttpResponse(template.render({'post': post}))


# About page
def about(request):

	template = loader.get_template('page-about.html')

	# Calculate my age to the nearest... well, whatever
	#	439624800	- Dec. 7th, 1983 (approx. time) in UNIX time
	# 31536000	- Seconds in a year
	age = (time.time() - 439624800) / 31536000 

	return HttpResponse(template.render({'age': age}))


# Contact page
def contact(request):

	template = loader.get_template('page-contact.html')

	# If the form has been submitted...
	if request.method == 'POST':

		# A form bound to the POST data
		form = ContactForm(request.POST)

		# All validation rules pass
		if form.is_valid():

			# Process the data in form.cleaned_data
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			message = form.cleaned_data['message']

			fullBody = 'Name: ' + name + ' - ' + email + '\nMessage:\n' + message

			recipients = [ settings.CONTACT_EMAIL ]

			from django.core.mail import send_mail
			send_mail(settings.CONTACT_SUBJECT, fullBody, settings.CONTACT_SENDER, recipients)

			# Redirect after POST
			return HttpResponseRedirect(reverse('contacted'))

	else:
		# Get an unbound form
		form = ContactForm() 

	return HttpResponse(template.render({'form': form}, request))
