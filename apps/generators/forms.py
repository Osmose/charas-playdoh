from PIL import Image

from django import forms

from tower import ugettext_lazy as _lazy

from generators.models import Part, Resource


INCORRECT_SIZE = _lazy(u'Incorrect size, image must be %sx%s pixels.')


class ResourceForm(forms.ModelForm):
    def __init__(self, generator, *args, **kwargs):
        super(ResourceForm, self).__init__(*args, **kwargs)

        self.fields['part'].empty_label = None

        self.generator = generator
        parts = Part.objects.filter(generator=generator)
        self.fields['part'].queryset = parts

    class Meta:
        model = Resource
        exclude = ('approved', 'created', 'modified', 'user')

    def clean_resource(self):
        resource = self.cleaned_data['resource']
        img = Image.open(resource)
        g = self.generator

        # Check dimensions
        dimensions = (g.resource_width, g.resource_height)
        if img.size != dimensions:
            raise forms.ValidationError(INCORRECT_SIZE % dimensions)

        return resource
