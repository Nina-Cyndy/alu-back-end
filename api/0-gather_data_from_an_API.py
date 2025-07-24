#!/usr/bin/python3
"""
Script to retrieve TODO list progress for a given employee ID
using a REST API.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    # Fetch user data
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)

    if user_response.status_code != 200:
        print("User not found.")
        sys.exit(1)

    user = user_response.json()
    employee_name = user.get("name")

    # Fetch todos
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)

    if todos_response.status_code != 200:
        print("Could not retrieve TODOs.")
        sys.exit(1)

    todos = todos_response.json()
    total_tasks = len(todos)
    completed_tasks = [task for task in todos if task.get("completed")]

    # Display progress
    print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task.get('title')}")
