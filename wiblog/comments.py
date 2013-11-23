from django.forms import ModelForm
from wiblog.models import Comment

class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = ('name', 'url', 'comment')

#	def __init__(self, *args, **kwargs):
#			user = kwargs.pop('post','')
#			super(DocumentForm, self).__init__(*args, **kwargs)
#			self.fields['user_defined_code']=forms.ModelChoiceField(queryset=UserDefinedCode.objects.filter(owner=user))
