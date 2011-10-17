from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS

from resources.models import Category, Resource


class CategoryResource(ModelResource):
    resources = fields.ToManyField('resources.api.ResourceResource',
                                   'resource_set')

    class Meta:
        queryset = Category.objects.all()
        resource_name = 'category'
        filtering = {'maker': ALL, 'slug': ALL}


class ResourceResource(ModelResource):
    category = fields.ToOneField(CategoryResource, 'category')

    class Meta:
        queryset = Resource.objects.filter(approved=True)
        resource_name = 'resource'
        filtering = {'category': ALL_WITH_RELATIONS}
        ordering = ['created']