# admin.py

from django.contrib import admin
from .models import TodoItem

@admin.register(TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed')
    list_filter = ('completed',)
    search_fields = ('title', 'description')
    list_editable = ('completed',)
