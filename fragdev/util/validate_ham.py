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

from django.core.exceptions import ValidationError

ANTI_SPAM = 'toothbrush'

def validate_ham(value):
    """
    Validate that the anti-spam value entered in matches the required one
    """
    if value != ANTI_SPAM:
        raise ValidationError('Anti-spam value incorrect: you may be a robot')
