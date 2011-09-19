from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

import jingo

from generators.forms import ResourceForm
from generators.models import Generator


def gen_app(request, slug):
    generator = get_object_or_404(Generator, slug__exact=slug)

    params = {'generator': generator}
    return jingo.render(request, 'generators/app.html', params)


@login_required
def upload(request, slug):
    generator = get_object_or_404(Generator, slug__exact=slug)
    form = ResourceForm(data=request.POST or None, generator=generator)
    if request.POST and form.is_valid():
        resource = form.save(commit=False)
        resource.user = request.user
        resource.save()
        # TODO: Finish upload

    params = {'generator': generator, 'form': form}
    return jingo.render(request, 'generators/upload.html', params)
