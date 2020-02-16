from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .forms import TodoForm
from .models import Todo

def index(request):
    mytodo = Todo.objects.order_by('id')
    form = TodoForm()
    context = {'mytodo':mytodo,'form':form}
    return render(request, 'index.html', context)


@require_POST
def add_new_todo(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        my_new_todo = Todo(todotext=request.POST['text'])
        my_new_todo.save()
    return redirect('todo:index')


def complete_todo(request, todo_id):
    mytodo = Todo.objects.get(pk=todo_id)
    mytodo.complete = True
    mytodo.save()
    return redirect('todo:index')

def delete_todo(request):
    Todo.objects.filter(complete__exact=True).delete()
    return redirect('todo:index')
