#!/usr/bin/python3
"""
Returns information about an employee's TODO list progress using their employee ID.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"UsageError: python3 {__file__} employee_id(int)")
        sys.exit(1)

    url_req = "https://jsonplaceholder.typicode.com"
    employee_id = sys.argv[1]

    response = requests.get(
        f"{url_req}/users/{employee_id}/todos",
        params={"_expand": "user"}
    )
    data = response.json()

    if not len(data):
        print("RequestError:", 404)
        sys.exit(1)

    employee_name = data[0]["user"]["name"]
    total_tasks = len(data)
    done_tasks = [task for task in data if task["completed"]]
    total_done_tasks = len(done_tasks)

    print(f"Employee {employee_name} is done with tasks"
          f"({total_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task['title']}")