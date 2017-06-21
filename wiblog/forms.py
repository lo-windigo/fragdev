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
from fragdev.util.validate_ham import ANTI_SPAM, validate_ham
from . import models


class CommentForm(forms.ModelForm):
    """
    Allow visitors to leave comments
    """
    verify = forms.CharField(label='Anti-spam: Type in the word "{}"'\
        .format(ANTI_SPAM),
        validators=[validate_ham],
        max_length=len(ANTI_SPAM))

    class Meta:
        model = models.Comment
        fields = ('name', 'url', 'comment')

