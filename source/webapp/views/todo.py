from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic.edit import UpdateView, DeleteView

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
            todo = ToDo.objects.create(**form.cleaned_data)
            reverse_url = reverse('todo_detail', kwargs={'pk': todo.pk})
            return redirect(reverse_url)


class DetailView(View):
    def get(self, request: WSGIRequest, pk):
        todo = get_object_or_404(ToDo, pk=pk)
        return render(request, 'todo.html', context={
            'todo': todo
        })


class ToDoUpdateView(View):
    def get(self, request, pk):
        todo = get_object_or_404(ToDo, pk=pk)
        return render(request, 'update_todo.html', context={'todo': todo})

    def post(self, request, pk):
        todo = get_object_or_404(ToDo, pk=pk)
        todo.title = request.POST.get('title')
        todo.author = request.POST.get('author')
        todo.text = request.POST.get('text')
        todo.save()
        return redirect('article_detail', pk=todo.pk)


class ToDoDeleteView(View):
    def post(self, request, pk):
        todo = get_object_or_404(ToDo, pk=pk)
        return render(request, 'todo_confirm_delete.html', context={'todo': todo})


def confirm_delete(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    todo.delete()
    return redirect('index')