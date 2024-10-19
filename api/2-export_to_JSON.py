#!/usr/bin/python3

import requests
import sys
import json

def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch the employee details
    user_url = f"{base_url}/users/{employee_id}"
    user_response = requests.get(user_url)
    
    if user_response.status_code != 200:
        print("Error: Unable to fetch employee details")
        return

    user_data = user_response.json()
    employee_name = user_data['name']
    username = user_data['username']

    todos_url = f"{base_url}/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)

    if todos_response.status_code != 200:
        print("Error: Unable to fetch TODO list")
        return

    todos_data = todos_response.json()

    # Calculate the number of completed and total tasks
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task['completed']]
    number_of_done_tasks = len(done_tasks)

    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")

    for task in done_tasks:
        print(f"\t {task['title']}")

    tasks_list = [{"task": task["title"], "completed": task["completed"], "username": username} for task in todos_data]
    json_data = {str(employee_id): tasks_list}

    # Export tasks to JSON file
    json_filename = f"{employee_id}.json"
    with open(json_filename, mode='w', encoding='utf-8') as file:
        json.dump(json_data, file, indent=4)

    print(f"Data exported to {json_filename}.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: employee_id must be an integer")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
