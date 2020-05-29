from __future__ import absolute_import, unicode_literals

from celery import shared_task
from celery.decorators import periodic_task
from celery.task.schedules import crontab
import requests

from requests.exceptions import HTTPError

from .models import WorkshopCached, UserMap

import json

import datetime


@shared_task
def fetch_data():
    url = 'localhost:5000'
    params = {'status': 1}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        response_data = response.json()  #Json_data_received
        workshop_id = response_data['id']  #later used for caching
        workshop_username = response_data['instructor']  #for user mapping
        Userobj = UserMap.objects.get(workshopUsername=workshop_username)
        #get the yaksh username from this.
        #prepare the data and send the post request
        post_url = r'http://localhost:8000/api/course/create/'
        try:
            with open('demo-data.json') as f:
                json_data = json.load(f)
            #prepare the json_data to be sent to post api.
            yaksh_user = Userobj.yayakshUsername
            course_info = {}
            course_info['name'] = response_data['name']  #course name
            course_info['creator'] = yaksh_user  #course creator
            course_info['created_on'] = response_data[
                'date']  #course created on
            course_info['start_enroll_time'] = response_data[
                'date']  #course start date
            course_duration = response_data['duration']
            course_duration_days = course_duration.find('days')
            course_duration = int(course_duration[:course_duration_days])
            course_info['end_enroll_time'] = response_data[
                'date'] + datetime.timedelta(
                    days=course_duration)  #course end date
            #Course basic info data is prepared now join with learning module
            course_info.update(
                json_data
            )  #learnin module data is appended in course_info dict
            post_response = requests.post(post_url, json=course_info)
            if post_response:
                #update the workshop cached with a new entry.
                WorkshopCached.objects.create(id=workshop_id)
            # If the response was successful, no Exception will be raised
            post_response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Python 3.6
        except Exception as err:
            print(f'Other error occurred: {err}')  # Python 3.6
        else:
            print('Request Success!')  #The request was successful.
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Request Success!')  #The request was successful.
