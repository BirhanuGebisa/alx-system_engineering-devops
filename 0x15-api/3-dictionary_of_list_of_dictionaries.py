#!/usr/bin/python3
"""Python script to export data in the JSON format"""

import json
import requests

if __name__ == "__main__":

    emplotee_data = requests.get('https://jsonplaceholder.typicode.com/users')
    task_data = requests.get('https://jsonplaceholder.typicode.com/todos')

    data = {}
    for user in emplotee_data.json():
        task_list = []
        for task in task_data.json():
            new_task = {}
            if task.get('userId') == user.get('id'):
                new_task['task'] = task.get('title')
                new_task['completed'] = task.get('completed')
                new_task['username'] = user.get('username')
                task_list.append(new_task)
        data['{}'.format(user.get('id'))] = task_list
    # Create file
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(data, json_file)
