from django.contrib import admin

from funfactory.admin import site

from generators.models import Generator, Part, Resource


class GeneratorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
site.register(Generator, GeneratorAdmin)


class PartAdmin(admin.ModelAdmin):
     prepopulated_fields = {'slug': ('name',)}
     list_display = ('name', 'generator', 'order')
     list_editable = ('order',)
     list_filter = ('generator',)
site.register(Part, PartAdmin)


def preview_img(resource):
    """Returns an HTML image of the resource's preview image."""
    return '<img src="%s">' % resource.preview
preview_img.allow_tags = True


class ResourceAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'part', 'approved', preview_img)
    list_editable = ('approved',)
    list_filter = ('part', 'part__generator')
site.register(Resource, ResourceAdmin)
