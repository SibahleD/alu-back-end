#!/usr/bin/python3

"""
Returns information about an employee's TODO list progress using their employee ID.
"""

import requests
import sys

def get_employee_todo_progress(employee_id):
    # Fetch employee details
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    user_response = requests.get(user_url)
    
    if user_response.status_code != 200:
        print(f"Employee with ID {employee_id} not found.")
        return

    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Fetch employee TODO list
    todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    todos_response = requests.get(todos_url)

    if todos_response.status_code != 200:
        print("Failed to fetch TODO list for employee.")
        return

    todos = todos_response.json()

    # Calculate completed and total tasks
    completed_tasks = [todo for todo in todos if todo.get('completed')]
    total_tasks = len(todos)
    completed_task_count = len(completed_tasks)

    # Display the output
    print(f"Employee {employee_name} is done with tasks({completed_task_count}/{total_tasks}):")
    
    # Print completed task titles
    for task in completed_tasks:
        print(f"\t {task.get('title')}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_progress(employee_id)