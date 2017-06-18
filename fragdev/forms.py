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
