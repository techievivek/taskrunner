from __future__ import absolute_import, unicode_literals

from celery import shared_task

import requests

from requests.exceptions import HTTPError

from .models import WorkshopCached
@shared_task
def fetch_data():
    url = 'localhost:5000'
    params = {'status': 1}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        response_data = response.json()  #Json_data_received
        workshop_id=response_data['id']
        workshop_username=response_data['username']
        #get the yaksh username from this.
        #prepare the data and send the post request

        post_url='localhost:8000'
        data=None
        post_response=requests.post(url,data=data)
        if post_response:
            WorkshopCached.objects.create(id=workshop_id)
            
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
