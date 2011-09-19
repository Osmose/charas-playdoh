from django import forms

from generators.models import Part, Resource


class ResourceForm(forms.ModelForm):
    def __init__(self, generator=None, *args, **kwargs):
        super(ResourceForm, self).__init__(*args, **kwargs)

        self.fields['part'].empty_label = None
        if generator is not None:
            parts = Part.objects.filter(generator=generator)
            self.fields['part'].queryset = parts

    class Meta:
        model = Resource
        exclude = ('approved', 'created', 'modified', 'user')
