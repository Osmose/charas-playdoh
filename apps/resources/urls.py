from django.conf.urls.defaults import include, patterns, url

from tastypie.api import Api

from resources import views
from resources.api import ResourceResource


# Set up REST resources
v1_api = Api(api_name='v1')
v1_api.register(ResourceResource())



urlpatterns = patterns('',
    url(r'^$', views.app, name='resources'),
    (r'^api/', include(v1_api.urls)),
)
