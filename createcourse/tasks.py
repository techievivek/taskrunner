from __future__ import absolute_import, unicode_literals

from celery import shared_task
from celery.decorators import periodic_task
from celery.task.schedules import crontab
import requests

from requests.exceptions import HTTPError

from .models import WorkshopCached,UserMap

import json

@periodic_task(
    run_every=(
        crontab(
            hour='*', minute='*', day_of_week='*', day_of_month='*',
            month_of_year='*'
        )
    ), name='Fetch data from workshop site'
)
def fetch_data():
    return 2
    url = 'localhost:5000'
    params = {'status': 1}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        response_data = response.json()  #Json_data_received
        workshop_id = response_data['id']
        workshop_username = response_data['username']
        Userobj=UserMap.objects.get(workshopUsername=workshop_username)
        #get the yaksh username from this.
        #prepare the data and send the post request
        post_url = r'http://localhost:8000/api/course/create/'
        try:
            with open('demo-data.json') as f:
                json_data = json.load(f)
            #prepare the json_data to be sent to post api.
            yaksh_user=Userobj.yayakshUsername
            response = requests.post(post_url, json=json_data)
            if response:
                #update the workshop cached with a new entry.
                WorkshopCached.objects.create(id=workshop_id)
            # If the response was successful, no Exception will be raised
            response.raise_for_status()
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

