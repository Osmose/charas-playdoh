from django.shortcuts import render

from gamemakers import GAMEMAKERS

from resources.models import Category


def app(request):
    gamemakers = []
    for slug, data in GAMEMAKERS.items():
        gamemakers.append({
            'name': data['name'],
            'categories': Category.objects.filter(maker=slug),
        })

    params = {
        'gamemakers': gamemakers,
    }
    return render(request, 'resources/app.html', params)
