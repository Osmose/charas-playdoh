from tastypie.resources import ModelResource, ALL_WITH_RELATIONS

from resources.models import Resource


class ResourceResource(ModelResource):
    class Meta:
        queryset = Resource.objects.filter(approved=True)
        resource_name = 'resource'
        filtering = {'category': ALL_WITH_RELATIONS}
