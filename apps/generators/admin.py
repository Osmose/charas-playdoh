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


class ResourceAdmin(admin.ModelAdmin):
    pass
site.register(Resource, ResourceAdmin)
