import urllib

from django.conf import settings
from django.contrib.auth.models import User
from django.utils.hashcompat import md5_constructor

from jingo import register
from jinja2 import Markup


GRAVATAR_URL = getattr(settings, 'GRAVATAR_URL', 'http://www.gravatar.com')


@register.function
def gravatar_url(arg, size=80):
    if isinstance(arg, User):
        email = arg.email
    else:  # Treat as email
        email = arg

    url = '%s/avatar/%s?' % (GRAVATAR_URL, md5_constructor(email).hexdigest())
    url += urllib.urlencode({'s': str(size)})

    return url


@register.function
def gravatar_img(arg, size=80):
    return Markup('<img src="%s">' % gravatar_url(arg, size=size))
