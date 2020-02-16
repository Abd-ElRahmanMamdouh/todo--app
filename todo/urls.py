from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add_new_todo, name='add'),
    path('complete/<todo_id>', views.complete_todo, name='complete'),
    path('delete', views.delete_todo, name='delete'),
]
