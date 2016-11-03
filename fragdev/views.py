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
	project = False

	# Try to get the latest blog post
	if 'wiblog' in settings.INSTALLED_APPS:
		from wiblog.models import Post
		from wiblog.formatting import mdToHTML, summarize

		if Post.objects.count() > 0:
			post = Post.objects.filter(status=Post.PUB).order_by('-date')[0]
			post.body = mdToHTML(summarize(post.body))

	# Try to get the latest project
	if 'projects' in settings.INSTALLED_APPS:
		from projects.models import Project

		if Project.objects.count() > 0:
			project = Project.objects.exclude(status=Project.HIDDEN).order_by('-date')[0]

	return HttpResponse(template.render({
            'post': post,
            'project': project
            }))


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
