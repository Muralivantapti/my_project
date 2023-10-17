from django.test import TestCase
from django.urls import reverse
from .models import TodoItem
from .forms import TodoItemForm

class TodoItemModelTest(TestCase):
    def test_create_todo_item(self):
        todo = TodoItem(title='Test Todo Item')
        todo.save()
        self.assertEqual(todo.title, 'Test Todo Item')
        self.assertFalse(todo.completed)

class TodoItemViewTest(TestCase):
    def test_todo_list_view(self):
        response = self.client.get(reverse('todo_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo_list.html')

    def test_todo_item_creation(self):
        response = self.client.post(reverse('add_task'), {'task': 'New Task'})
        self.assertEqual(response.status_code, 302)  # 302 is the code for a redirect
        self.assertEqual(TodoItem.objects.count(), 1)

    def test_todo_item_deletion(self):
        todo = TodoItem(title='Test Task')
        todo.save()
        response = self.client.get(reverse('delete_task', args=(todo.id,)))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(TodoItem.objects.count(), 0)

class TodoItemFormTest(TestCase):
    def test_todo_item_form(self):
        form_data = {'title': 'Form Task'}
        form = TodoItemForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_todo_item_form_invalid(self):
        form_data = {'title': ''}
        form = TodoItemForm(data=form_data)
        self.assertFalse(form.is_valid())
