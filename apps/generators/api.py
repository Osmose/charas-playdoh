from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS

from generators.models import Part, Resource


class PartResource(ModelResource):
    resources = fields.ToManyField('generators.api.ResourceResource',
                                   'resource_set')
    class Meta:
        queryset = Part.objects.all()
        resource_name = 'part'
        filtering = {'generator': ALL_WITH_RELATIONS, 'slug': ALL}


class ResourceResource(ModelResource):
    part = fields.ToOneField(PartResource, 'part')
    class Meta:
        queryset = Resource.objects.all()
        resource_name = 'resource'
        filtering = {'part': ALL_WITH_RELATIONS}
