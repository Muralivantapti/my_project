from django.urls import path
from . import views

app_name = 'todo'  # optional if you have multiple apps

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('add_task/', views.add_task, name='add_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
    # You can define more URLs for your application as needed
]

