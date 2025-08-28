from django.test import TestCase
from django.urls import reverse
from .models import Task
from .forms import TaskForm

# Create your tests here.

class TaskModelTest(TestCase):
    def test_task_creation(self):
        task = Task.objects.create(title='Test Task')
        self.assertEqual(task.title, 'Test Task')
        self.assertFalse(task.complete)
    
    def test_str_representation(self):
        task = Task(title="Clean Room")
        self.assertEqual(str(task), "Clean Room")


class TaskFormTest(TestCase):
    def test_valid_form(self):
        form = TaskForm(data={'title': 'Buy Milk', 'complete': False})
        self.assertTrue(form.is_valid())
    
    def test_invalid_form(self):
        form = TaskForm(data={'title': '', 'complete': False})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)


class TaskViewTest(TestCase):
    def setUp(self):
        self.task = Task.objects.create(title="Initial Task")

    def test_list_view_status_code(self):
        response = self.client.get(reverse('list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/list.html')
    
    def test_create_task(self):
        response = self.client.post(reverse('list'), {
            'title': 'New Task'
        })
        self.assertEqual(Task.objects.count(), 2)
        self.assertRedirects(response, reverse('list'))

    def test_update_task(self):
        response = self.client.post(reverse('update_task', args=[self.task.id]), {
            'title': 'Updated Task',
            'complete': True
        })
    
    def test_delete_task(self):
        response = self.client.post(reverse('delete_task', args=[self.task.id]))
        self.assertEqual(Task.objects.count(), 0)
        self.assertRedirects(response, reverse('list'))
        