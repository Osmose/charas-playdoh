from django.contrib import admin

from funfactory.admin import site

from resources.models import Category, Resource


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'maker', 'resource_type')
site.register(Category, CategoryAdmin)


class ResourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'category',  'approved')
    list_editable = ('approved',)
site.register(Resource, ResourceAdmin)
