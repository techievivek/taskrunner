from __future__ import absolute_import, unicode_literals
import celery
from celery.task.schedules import crontab
import requests

from requests.exceptions import HTTPError

from .models import WorkshopCached, UserMap

import json

import datetime

from .api_settings import workshop_url, yaksh_post_url, workshop_json_file_mapper
import os

from django_celery_results.models import TaskResult

@celery.task
def fetch_data():
    params = {'status': 1}
    last_fetched_task=TaskResult.objects.order_by('-date_done')
    if len(last_fetched_task):
        params['date_from']=last_fetched_task[0].date_done.strftime('%Y-%m-%d')
    else:
        params['date_from']=datetime.date.today().strftime('%Y-%m-%d')
    try:
        response = requests.get(workshop_url, params=params)
        response.raise_for_status()
        response_data = response.json(
        )  #Data recieved and converted into python objects.
        #There can be multiple workshops so iterate over all
        for res_data in response_data:
            workshop_id = res_data['id']  #later used for caching
            cached_workshop = WorkshopCached.objects.create(id=workshop_id,
                                                            status=0)
            workshop_username = res_data['instructor']  #for user mapping
            Userobj = UserMap.objects.get(workshop_user=workshop_username)
            #get the yaksh username from this.
            #prepare the data and send the post request
            course_info = {}
            course_info['name'] = res_data['name']  #course name
            course_info['creator'] = Userobj.yaksh_user  #course creator
            course_info['created_on'] = res_data['date']  #course created on
            course_info['start_enroll_time'] = res_data[
                'date']  #course start date
            course_duration = res_data['duration']
            course_duration_days = course_duration.find('days')
            course_duration = int(course_duration[:course_duration_days])
            course_info[
                'end_enroll_time'] = res_data['date'] + datetime.timedelta(
                    days=course_duration)  #course end date
            #Course basic info data is prepared now join with learning module
            with open(
                    os.path.join(
                        'fixtures',
                        workshop_json_file_mapper[str(course_duration)])) as f:
                json_data = json.load(f)
            course_info.update(
                json_data
            )  #learning module data is appended in course_info dict
            post_response = requests.post(yaksh_post_url, json=course_info)
            if post_response.status_code == 201:
                #update the workshop cached with a new entry.
                cached_workshop.status = 1
                cached_workshop.save()
            else:
                cached_workshop.status = 2
                cached_workshop.save()
                print("Something went wrong during post request.")
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
