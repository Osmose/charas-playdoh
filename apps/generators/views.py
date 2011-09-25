from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from generators.forms import ResourceForm
from generators.models import Generator


def gen_app(request, slug):
    generator = get_object_or_404(Generator, slug__exact=slug)

    params = {'generator': generator}
    return render(request, 'generators/app.html', params)


@login_required
def upload(request, slug):
    generator = get_object_or_404(Generator, slug__exact=slug)
    form = ResourceForm(generator, request.POST or None, request.FILES)
    if request.POST and form.is_valid():
        resource = form.save(commit=False)
        resource.user = request.user
        resource.save()
        return render(request, 'generators/upload_complete.html')

    params = {'generator': generator, 'form': form}
    return render(request, 'generators/upload.html', params)
