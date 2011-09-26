import jingo

from charas_project.models import FrontPageFeature


def home(request):
    params = {
        'features': (FrontPageFeature.objects.filter(enabled=True)
                     .order_by('-created')),
    }
    return jingo.render(request, 'charas_project/home.html', params)
