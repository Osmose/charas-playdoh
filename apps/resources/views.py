import json

from django.shortcuts import render

from gamemakers import GAMEMAKERS

from resources.models import Category


def app(request):
    gamemakers = []
    for slug, data in GAMEMAKERS.items():
        categories = []
        for category in Category.objects.filter(maker=slug):
            categories.append({
                'name': category.name,
                'slug': category.slug,
                'maker': slug,
            })

        gamemakers.append({
            'name': unicode(data['name']),
            'slug': slug,
            'categories': categories,
        })

    params = {
        'gamemakers': json.dumps(gamemakers),
    }
    return render(request, 'resources/app.html', params)
