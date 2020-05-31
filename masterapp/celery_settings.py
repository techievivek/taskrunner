import os
from django.conf import settings
from celery import Celery
from celery.schedules import crontab
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'masterapp.settings')

app = Celery('masterapp')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

#Task schedule settings
app.conf.beat_schedule = {
    # Executes every  Minute
    'Fetch data from workshop site': {
        'task': 'createcourse.tasks.fetch_data',
        'schedule': crontab(hour='*', minute='*/1', day_of_week='*'),
    },
}