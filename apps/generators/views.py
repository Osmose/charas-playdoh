import jingo

from generators.models import Generator


def gen_app(request, slug):
    generator = Generator.objects.get(slug__exact=slug)

    params = {'generator': generator}
    return jingo.render(request, 'generators/app.html', params)
