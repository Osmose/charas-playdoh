import re

from django import forms
from django.forms.util import ValidationError
from django.contrib.auth.models import User

from tower import ugettext_lazy as _lazy


PASSWD_REQUIRED = _lazy(u'Please enter a password.')
PASSWD_MATCH = _lazy(u'Passwords must match.')
PASSWD_LENGTH = _lazy(u'Passwords must be at least 8 characters long.')
PASSWD_COMPLEX = _lazy(u'Passwords must contain at least 1 letter and '
                       '1 number.')


class PasswordField(forms.CharField):
    """Field for displaying a password input."""

    error_messages = {
        'min_length': PASSWD_LENGTH,
        'required': PASSWD_REQUIRED,
    }

    def __init__(self, *args, **kwargs):
        defaults = {
            'label': _lazy(u'Password'),
            'widget': forms.PasswordInput(render_value=False),
            'min_length': 8,
            'error_messages': PasswordField.error_messages,
        }
        defaults.update(kwargs)
        return super(PasswordField, self).__init__(*args, **defaults)

    def clean(self, value):
        """Passwords must consist of letters and numbers."""
        cleaned_value = super(PasswordField, self).clean(value)

        if cleaned_value:
            # Unicode letters are anything in \w that isn't a digit or _
            letters = re.search(r'(?Lu)[^\W\d_]+', cleaned_value)
            numbers = re.search(r'(?Lu)\d+', cleaned_value)
            if not (letters and numbers):
                raise ValidationError(PASSWD_COMPLEX)

        return cleaned_value


class RegistrationForm(forms.ModelForm):
    password = PasswordField()

    class Meta:
        model = User
        fields = ('username', 'email')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
