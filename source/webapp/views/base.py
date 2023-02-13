from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from webapp.models import ToDo


def index_view(request: WSGIRequest):
    todo = ToDo.objects.all()
    context = {
        'todo': todo
    }
    return render(request, 'index.html', context=context)