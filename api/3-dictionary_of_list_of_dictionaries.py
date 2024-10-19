#!/usr/bin/python3

import requests
import json

def fetch_all_employees_todo():
    # Define the base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch the employee details
    users_url = f"{base_url}/users"
    users_response = requests.get(users_url)
    
    if users_response.status_code != 200:
        print("Error: Unable to fetch employees")
        return

    users_data = users_response.json()

    # Create a dictionary to store tasks by user
    all_tasks = {}

    # Fetch TODO list for each employee
    for user in users_data:
        user_id = user['id']
        username = user['username']

        # Fetch the employee's TODO list
        todos_url = f"{base_url}/todos?userId={user_id}"
        todos_response = requests.get(todos_url)

        if todos_response.status_code != 200:
            print(f"Error: Unable to fetch TODO list for user {user_id}")
            continue

        todos_data = todos_response.json()

        tasks_list = [{"username": username, "task": task["title"], "completed": task["completed"]} for task in todos_data]
        all_tasks[str(user_id)] = tasks_list

    # Export all tasks to a JSON file
    json_filename = "todo_all_employees.json"
    with open(json_filename, mode='w', encoding='utf-8') as file:
        json.dump(all_tasks, file, indent=4)

    print(f"Data exported to {json_filename}.")

if __name__ == "__main__":
    fetch_all_employees_todo()
