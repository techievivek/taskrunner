from django_celery_beat.models import CrontabSchedule, PeriodicTask
schedule, _ = CrontabSchedule.objects.get_or_create(
    minute='30',
    hour='*',
    day_of_week='*',
    day_of_month='*',
    month_of_year='*',
    timezone=pytz.timezone('Asia/Kolkata')
 )
PeriodicTask.objects.create(
     crontab=schedule,
     name='Fetch data from workshop site',
     task='createcourse.tasks.add',
     args=json.dumps(['args1', 'args2']), #'args1', 'args2'
 )

