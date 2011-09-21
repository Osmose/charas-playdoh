from django.contrib.auth import authenticate, login as auth_login, views
from django.shortcuts import render

from session_csrf import anonymous_csrf

from users.forms import RegistrationForm


@anonymous_csrf
def login(*args, **kwargs):
    return views.login(*args, **kwargs)


def profile(request):
    return render(request, 'users/profile.html')


@anonymous_csrf
def register(request):
    form = RegistrationForm(request.POST or None)
    if request.POST and form.is_valid():
        form.save()
        user = authenticate(username=request.POST['username'],
                            password=request.POST['password'])
        auth_login(request, user)
        return render(request, 'registration/register_complete.html')

    return render(request, 'registration/register.html', {'form': form})
