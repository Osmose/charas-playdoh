from django.contrib import admin

from funfactory.admin import site

from charas_project.models import FrontPageFeature


class FrontPageFeatureAdmin(admin.ModelAdmin):
    list_display = ('headline', 'author', 'created')

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()
site.register(FrontPageFeature, FrontPageFeatureAdmin)
