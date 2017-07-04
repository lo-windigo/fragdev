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

import smtplib
from email.mime.text import MIMEText
from django.conf import settings
from django.core.mail import send_mail
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render
from django.template.context_processors import csrf
from django.views import generic 
from django.views.generic import edit
from wiblog import forms, models


class IndexView(generic.ListView):
    """
    Blog index: Show a list of the most recent posts
    """
    context_object_name = 'posts'
    paginate_by = 5
    queryset = models.Post.published.order_by('-date')
    template_name = 'base-wiblog.html'


class ArchiveView(generic.ListView):
    """
    An archival listing of all public posts
    """
    context_object_name = 'posts'
    queryset = models.Post.published.all()
    template_name = 'page-archive.html'


class CommentView(edit.CreateView):
    """
    Processing comments
    """
    form_class = forms.CommentForm
    model = models.Comment
    success_url = reverse_lazy('comment-successful')
    template_name = 'page-comment.html'

    def form_valid(self, form):
        """
        If handling a valid form, make sure to email a notification to someone
        who can moderate it
        """
        sender = settings.CONTACT_SENDER
        sendee = settings.CONTACT_EMAIL

        msg = MIMEText('New Comment')
        msg['Subject'] = 'Comments awaiting moderation'
        msg['From'] = sender
        msg['To'] = sendee

        mailServer = smtplib.SMTP('localhost')
        mailServer.sendmail(sender, [sendee], msg.as_string())
        mailServer.quit

        return super().form_valid(form)


class PostView(generic.DetailView):
    """
    A single blog post
    """
    context_object_name = 'post'
    model = models.Post
    template_name = 'page-post.html'

    def get_context_data(self, **kwargs):
        """
        Add a comment form to the default context
        """
        context = super().get_context_data(**kwargs)

        # Send in a comment form
        context['comment_form'] = forms.CommentForm(initial={
            'post': self.object.pk,
            })

        return context


class TagsView(generic.ListView):
    """
    Display any blog tags that have been defined
    """
    context_object_name = 'tags'
    queryset = models.Tag.objects.order_by('desc')
    template_name = 'page-tags.html'


class TaggedPostView(generic.DetailView):
    """
    Show any posts that are associated with a tag
    """
    context_object_name = 'tag'
    model = models.Tag
    slug_field = 'desc'
    slug_url_kwarg = 'tag'
    template_name = 'page-tagged.html'

