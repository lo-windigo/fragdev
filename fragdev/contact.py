from django import forms
from django.core.exceptions import ValidationError

# Anti-spam validation
def validate_ham(value):
	if value != 'power':
		raise ValidationError('Anti-spam value incorrect: you may be a robot')

# The form for the Contact page
class ContactForm(forms.Form):
	name = forms.CharField(max_length=100)
	email = forms.EmailField()
	message	= forms.CharField(widget=forms.Textarea)
	verify = forms.CharField(label='Anti-spam: Type in the word "power"',validators=[validate_ham],max_length=5)
