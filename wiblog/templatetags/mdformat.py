from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
import markdown

register = template.Library()

# Convert markdown-formatted text to HTML
# Note: @stringfilter decorator converts all value args to strings
@stringfilter
@register.filter()
def markdownToHTML(value):
	return mark_safe(markdown.markdown(value, output_format="html5"))
