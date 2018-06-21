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
from django.core.mail import EmailMessage
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.template.context_processors import csrf
from django.urls import reverse, reverse_lazy
from fragdev import forms
import time


class HomeView(TemplateView):
    """
    The homepage; list the latest blog post, project, and some other
    pertinent information
    """
    template_name = 'page-home.html'

    def get_context_data(self, **kwargs):
        """
        Add latest blog post and latest project as context
        """
        context = super().get_context_data(**kwargs)

        # Get the latest blog post
        if 'wiblog' in settings.INSTALLED_APPS:
            from wiblog.models import Post

            try:
                context['post'] = Post.published.order_by('-date').first()
            except:
                pass

        # Try to get the latest project
        if 'projects' in settings.INSTALLED_APPS:
            from projects.models import Project

            try:
                projects = Project.objects.exclude(status=Project.HIDDEN)
                context['project'] = projects.order_by('-date')[0]
            except:
                pass

        return context


class AboutView(TemplateView):
    """
    About Me page
    """
    template_name = 'page-about.html'

    def get_context_data(self, **kwargs):
        """
        Calculate my age to the nearest... well, whatever
        439664400 - Dec. 7th, 1983, 11PM in UNIX time
        31536000  - Seconds in a year
        """
        context = super().get_context_data(**kwargs)
        context['age'] = (time.time() - 439664400) / 31536000 

        return context


class ContactView(FormView):
    """
    A neat way for people to email me through a HTML form
    """
    form_class = forms.ContactForm
    success_url = reverse_lazy('contacted')
    template_name = 'page-contact.html'
    MESSAGE_TEMPLATE = '''
Name: {} <{}>
Message:
{}
'''

    def form_valid(self, form):
        """
        Send email with cleaned_data from form
        """
        email = EmailMessage()
        contact_name = form.cleaned_data['name']
        contact_email = form.cleaned_data['email']
        contact_message = form.cleaned_data['message']

        # Set up the EmailMessage object
        email.body = self.MESSAGE_TEMPLATE.format(contact_name, contact_email,
                contact_message)
        email.to = [ settings.CONTACT_EMAIL ]
        email.subject = settings.CONTACT_SUBJECT
        email.from_email = settings.CONTACT_SENDER
        email.reply_to = [ form.cleaned_data['email'] ]

        email.send()

        return super().form_valid(form)

