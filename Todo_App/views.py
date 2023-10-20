from django.shortcuts import render
from .models import TodoItem

def todo_list(request):
    todo_items = TodoItem.objects.all()
    return render(request, 'todo/todo_list.html', {'todo_items': todo_items})

from django.http import HttpResponse


def add_task(request):
    task = 'Take Bath'  # Task description
    TodoItem.objects.create(task=task)  # Creating a new TodoItem object with the given task
    return HttpResponse('<h1>Task created</h1>')
