from django.conf import settings
from django.conf.urls.defaults import patterns, include
from django.contrib.admin import autodiscover

from funfactory import admin

# Autodiscover admin entries
autodiscover()

urlpatterns = patterns('',
    (r'', include('charas_project.urls')),
    (r'^generators/', include('generators.urls')),
    (r'^accounts/', include('users.urls')),
    (r'^admin/', include(admin.site.urls)),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
)

## In DEBUG mode, serve media files through Django.
if settings.DEBUG:
    # Remove leading and trailing slashes so the regex matches.
    media_url = settings.MEDIA_URL.lstrip('/').rstrip('/')
    urlpatterns += patterns('',
        (r'^%s/(?P<path>.*)$' % media_url, 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )
