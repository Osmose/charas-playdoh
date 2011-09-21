from django.conf.urls.defaults import patterns, url
from django.contrib.auth import views as auth_views

from users.views import login, profile, register


urlpatterns = patterns('',
    url(r'^login/$', login, name='users.login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'},
        name='users.logout'),
    url(r'^profile/$', profile, name='users.profile'),
    url(r'^register/$', register, name='users.register'),
)
