from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from webapp.models import ToDo

from webapp.forms import ToDoForm


class AddView(View):
    def get(self, request: WSGIRequest):
        form = ToDoForm()
        return render(request, 'todo_create.html', context={'form': form})

    def post(self, request: WSGIRequest):
        form = ToDoForm(data=request.POST)
        if not form.is_valid():
            return render(request, 'todo_create.html', context={'form': form})
        else:
            ToDo.objects.create(**form.cleaned_data)
            return redirect('index')


class DetailView(View):
    def get(self, request: WSGIRequest, pk):
        todo = get_object_or_404(ToDo, pk=pk)
        return render(request, 'todo.html', context={
            'todo': todo
        })


class ToDoUpdateView(View):
    def get(self, request, pk):
        todo = get_object_or_404(ToDo, pk=pk)
        form = ToDoForm(instance=todo)
        return render(request, 'update_todo.html', context={'form': form, 'todo': todo})

    def post(self, request, pk):
        todo = get_object_or_404(ToDo, pk=pk)
        form = ToDoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'update_todo.html', context={'form': form})


class ToDoDeleteView(View):
    def get(self, request, pk):
        todo = get_object_or_404(ToDo, pk=pk)
        return render(request, 'todo_confirm_delete.html', context={'todo': todo})


def confirm_delete(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    todo.delete()
    return redirect('index')
