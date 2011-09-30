from django.conf.urls.defaults import patterns, url

from resources import views


urlpatterns = patterns('',
    url(r'^$', views.frontpage, name='resources'),
)
