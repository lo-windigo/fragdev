from django.utils.safestring import mark_safe
import CommonMark


# Convert a markdown string into HTML5, and prevent Django from escaping it
def mdToHTML(value):

    return mark_safe(CommonMark.commonmark(value))


# Get a summary of a post
def summarize(fullBody):

    firstNewline = fullBody.find("\n")

    if firstNewline > 0:
        return fullBody[:firstNewline]

    return fullBody
