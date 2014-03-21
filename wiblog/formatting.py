from django.utils.safestring import mark_safe
import markdown


# Convert a markdown string into HTML5, and prevent Django from escaping it
def mdToHTML(value):
	return mark_safe(markdown.markdown(value, output_format="html5"))


# Get a summary of a post
def summarize(fullBody):
	firstNewline = fullBody.find("\n")

	if firstNewline > 0:
		return unicode(fullBody)[:firstNewline]

	return fullBody
