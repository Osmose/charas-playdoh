from django.contrib.auth import views
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

from session_csrf import anonymous_csrf


@anonymous_csrf
def login(*args, **kwargs):
    return views.login(*args, **kwargs)


def profile(request):
    return render(request, 'users/profile.html')


@anonymous_csrf
def register(request):
    form = UserCreationForm(request.POST or None)
    if request.POST and form.is_valid():
        form.save()
        return render(request, 'users/register_complete.html')

    return render(request, 'users/register/html', {'form': form})
