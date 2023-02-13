from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect

from webapp.models import ToDo


def add_view(request: WSGIRequest):
    if request.method == 'GET':
        return render(request, 'todo_create.html')
    print(request.POST)
    todo_data = {
        'description': request.POST.get('description'),
        'status': request.POST.get('status'),
        'completion_at': request.POST.get('completion_at')
    }
    todo = ToDo.objects.create(**todo_data)
    return redirect(f'/todo/?pk={todo.pk}')


def detail_view(request):
    todo_pk = request.GET.get('pk')
    todo = ToDo.objects.get(pk=todo_pk)
    context = {'todo': todo}
    return render(request, 'todo.html', context=context)
