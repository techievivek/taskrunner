from django.test import TestCase
from django_celery_results.models import TaskResult
from .tasks import fetch_data


class TestFetchDataTask(TestCase):
    def setUp(self):
        self.task = fetch_data.delay()
        self.result=self.task.get()

    def test_task_state(self):
        self.assertEqual(self.task.state, 'SUCCESS')

    def test_task_result(self):
        t = TaskResult.objects.order_by('-date_done').first()
        self.assertEqual(t.status, 'SUCCESS')

    def clean_up_models(self):
        TaskResult.objects.all().delete()
