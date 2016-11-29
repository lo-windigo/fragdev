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

from django.template.context_processors import csrf
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render
from wiblog.util.formatting import render_markdown
from wiblog.models import Comment, Post, Tag
from wiblog.util.comments import CommentForm


def index(request):
    """ Blog index: Show a list of the most recent posts
    """

    # Get the 5 latest posts
    posts = Post.objects.filter(status=Post.PUB).order_by('-date')[:5]

    # Go through all the posts and format the post body
    for post in posts:
        post.body = render_markdown(post.body)

    return render(request, 'base-wiblog.html', {'posts': posts}))


def archive(request):
    """ An archival listing of all public posts
    """

    posts = Post.objects.filter(status=Post.PUB)

    return render(request, 'page-archive.html', template.render({'posts': posts}))


def post(request, slug):
    """ A single blog post
    """

    template = loader.get_template()

    # Try to get the requested post
    post = get_object_or_404(Post, slug=slug)

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
    post.body = render_markdown(post.body)

    # Format the comments for display
    for comment in comments:
        comment.comment = render_markdown(comment.comment)

    return render(request,
        'page-post.html',
        {
            'form': form,
            'post': post,
            'comments': comments
        })


def tags(request):
    """ Display any blog tags that have been defined
    """
    
    # Get any tags that have been defined
    tags = Tag.objects.order_by('desc')

    return HttpResponse(request, 'page-tags.html', {'tags': tags})


def tagged_posts(request, tag):
    """ Show any posts that are associated with a tag
    """

    tagObj = get_object_or_404(Tag, desc=tag)
    posts = Post.objects.filter(tags=tagObj,status=Post.PUB)

    # Go through all the posts, trim and format the post body
    for post in posts:
        post.body = render_markdown(post.body)

    return render(request, 'page-tagged.html', {'posts': posts, 'tag': tagObj})
