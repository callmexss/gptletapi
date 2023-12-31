from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings
from dotenv import load_dotenv


load_dotenv()


DJ_SETTINGS = os.environ.get('DJ_SETTINGS', 'prod')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'gptletapi.settings.{DJ_SETTINGS}')

app = Celery('gptletapi')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {}
for task_name, task_config in settings.CELERY_BEAT_SCHEDULE.items():
    schedule = task_config.pop('schedule', {})
    minute = schedule.get('minute', '*')
    hour = schedule.get('hour', '*')
    day_of_week = schedule.get('day_of_week', '*')
    day_of_month = schedule.get('day_of_month', '*')
    month_of_year = schedule.get('month_of_year', '*')

    app.conf.beat_schedule[task_name] = {
        **task_config,
        'schedule': crontab(minute=minute, hour=hour, day_of_week=day_of_week,
                            day_of_month=day_of_month, month_of_year=month_of_year),
    }