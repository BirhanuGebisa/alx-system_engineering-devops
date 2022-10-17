#!/usr/bin/python3
"""Python script to export data in the JSON format"""

import json
import requests
import sys


if __name__ == "__main__":

    if sys.argv[1].isdigit():
        # user id
        user_id = sys.argv[1]

        # URLS to get data
        employee = requests.get('https://jsonplaceholder.typicode.com/users',
                                params={'id':  user_id}).json()
        tasks_todo = requests.get('https://jsonplaceholder.typicode.com/todos',
                                  params={'userId':  user_id}).json()
        username = employee[0]['username']

        data = {}
        task_list = []
        for each_task in tasks_todo:
            # create new dictionary just with required info
            dict_task = {}
            dict_task['task'] = each_task.get('title')
            dict_task['completed'] = each_task.get('completed')
            dict_task['username'] = username
            task_list.append(dict_task)
        data['{}'.format(user_id)] = task_list
        # Open file
        with open('{}.json'.format(user_id), 'w', newline='') as json_file:
            json.dump(data, json_file)
