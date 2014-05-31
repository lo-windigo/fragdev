from django.conf import settings
from django.core.context_processors import csrf
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, RequestContext, loader
from django.core.urlresolvers import reverse
from fragdev.contact import ContactForm
import time


def home(request):
	template = loader.get_template('base.html')
	context = Context()

	return HttpResponse(template.render(context))


# About page
def about(request):

	template = loader.get_template('base-about.html')

	# Calculate my age to the nearest... well, whatever
	#	439624800	- Dec. 7th, 1983 (approx. time) in UNIX time
	# 31536000	- Seconds in a year
	age = (time.time() - 439624800) / 31536000 
	context = Context({'age': age})

	return HttpResponse(template.render(context))


# About Me page
def aboutMe(request):

	template = loader.get_template('base-about-me.html')
	context = Context()

	return HttpResponse(template.render(context))


# About - Education page
def aboutEdu(request):

	template = loader.get_template('base-about-education.html')
	context = Context()

	return HttpResponse(template.render(context))


# About - Employment History page
def aboutEmp(request):

	template = loader.get_template('base-about-emp.html')
	context = Context()

	return HttpResponse(template.render(context))


# About - Portfolio page
def aboutPortfolio(request):

	template = loader.get_template('base-about-portfolio.html')
	context = Context()

	return HttpResponse(template.render(context))


# About - Skills page
def aboutSkills(request):

	template = loader.get_template('base-about-skills.html')
	context = Context()

	return HttpResponse(template.render(context))


# Contact page
def contact(request):

	template = loader.get_template('base-contact.html')

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

	context = RequestContext(request, {'form': form})

	return HttpResponse(template.render(context))


def contacted(request):
	template = loader.get_template('base-contacted.html')
	context = Context()

	return HttpResponse(template.render(context))


def projects(request):
	template = loader.get_template('base-projects.html')
	context = Context()

	return HttpResponse(template.render(context))


def resume(request):
	template = loader.get_template('base-resume.html')
	context = Context()

	return HttpResponse(template.render(context))
