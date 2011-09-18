from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('charas_project.views',
	url(r'^$', 'home', name='home'),
)