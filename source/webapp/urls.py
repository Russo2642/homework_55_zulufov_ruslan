from django.urls import path
from webapp.views.base import IndexView
from webapp.views.todo import AddView
from webapp.views.todo import DetailView
from webapp.views.todo import ToDoUpdateView
from webapp.views.todo import ToDoDeleteView

from webapp.views.todo import confirm_delete

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('todo/add/', AddView.as_view(), name='todo_add'),
    path('todo/<int:pk>', DetailView.as_view(), name='todo_detail'),
    path('todo/<int:pk>/update/', ToDoUpdateView.as_view(), name='todo_update'),
    path('todo/<int:pk>/delete/', ToDoDeleteView.as_view(), name='todo_delete'),
    path('todo/<int:pk>/confirm_delete/', confirm_delete, name='confirm_delete'),
]
