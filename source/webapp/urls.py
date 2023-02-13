from django.urls import path

from webapp.views.base import index_view

from webapp.views.todo import add_view

from webapp.views.todo import detail_view

urlpatterns = [
    path('', index_view),
    path('todo/add/', add_view),
    path('todo/', detail_view)
]
