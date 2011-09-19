from django.conf.urls.defaults import include, patterns, url

from tastypie.api import Api

from generators import views
from generators.api import PartResource, ResourceResource


# Set up REST resources
v1_api = Api(api_name='v1')
v1_api.register(PartResource())
v1_api.register(ResourceResource())


urlpatterns = patterns('',
    url(r'^(?P<slug>[\w-]+)$', views.gen_app, name='generators.gen_app'),
    url(r'^upload/(?P<slug>[\w-]+)$', views.upload, name='generators.upload'),
    (r'^api/', include(v1_api.urls)),
)
