from http import HTTPStatus

from api import models
from django.test import Client, TestCase


class TaskiAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_taskiapi(self):
        """Проверка доступности списка задач."""
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_task_creation(self):
        """Проверка создани задач."""
        data = {
            'title': 'Test',
            'description': 'Test',
        }
        response = self.client.post('/api/tasks/', data=data)
        self.assertEqual(response.status_code, HTTPStatus.CREATED)
        self.assertTrue(models.Task.objects.filter(title='Test').exists())
