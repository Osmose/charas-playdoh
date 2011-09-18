import jingo


def home(request):
	return jingo.render(request, 'charas_project/home.html')
