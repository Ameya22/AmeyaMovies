import os
import json
from django.shortcuts import render
from django.http import HttpResponse


def get_movies():
    try:
        json_obj = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)),  'movies_data', 'index.json'))
        fp = open(json_obj, 'r')
        return json.loads(fp.read())
    except Exception as err:
        print(err)
        return {}


def movies(request):
    movies_list = get_movies()
    return render(request, 'index.html', {'movies': movies_list})
