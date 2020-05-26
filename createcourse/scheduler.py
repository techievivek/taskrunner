from django_celery_beat.models import CrontabSchedule, PeriodicTask
import pytz
import json
schedule, _ = CrontabSchedule.objects.get_or_create(
    minute='*',
    hour='*',
    day_of_week='*',
    day_of_month='*',
    month_of_year='*',
    timezone=pytz.timezone('Asia/Kolkata'))
PeriodicTask.objects.create(
    crontab=schedule,
    name='Fetch data from workshop site',
    task='createcourse.tasks.add',
    args=json.dumps(['args1', 'args2']),
)
