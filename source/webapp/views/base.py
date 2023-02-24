from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from django.views import View

from webapp.models import ToDo


class IndexView(View):
    def get(self, request: WSGIRequest):
        todo = ToDo.objects.exclude(is_deleted=True)
        context = {
            'todo': todo
        }
        return render(request, 'index.html', context=context)
