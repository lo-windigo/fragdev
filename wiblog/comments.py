from fragdev.contact import validate_ham
from django.forms import ModelForm
from django import forms
from wiblog.models import Comment

class CommentForm(ModelForm):
	verify = forms.CharField(label='Anti-spam: Type in the word "power"',validators=[validate_ham],max_length=5)
	class Meta:
		model = Comment
		fields = ('name', 'url', 'comment')
