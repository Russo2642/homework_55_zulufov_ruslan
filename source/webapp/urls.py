from django.urls import path
from webapp.views.base import IndexView
from webapp.views.todo import AddView
from webapp.views.todo import DetailView
from webapp.views.todo import ToDoUpdateView

from webapp.views.todo import ToDoDeleteView

urlpatterns = [
    path('', IndexView.as_view()),
    path('todo/add/', AddView.as_view()),
    path('todo/', DetailView.as_view(), name='todo_detail'),
    path('todo/<int:pk>/update', ToDoUpdateView.as_view(), name='todo_update'),
    path('todo/<int:pk>/delete', ToDoDeleteView.as_view(), name='todo_delete')
]
