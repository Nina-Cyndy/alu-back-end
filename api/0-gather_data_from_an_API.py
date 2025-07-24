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

    # Get user information
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Employee not found.")
        sys.exit(1)

    employee_name = user_response.json().get("name")

    # Get TODOs for the user
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print("Could not fetch tasks.")
        sys.exit(1)

    todos = todos_response.json()
    done_tasks = [task for task in todos if task.get("completed")]
    total_tasks = len(todos)
    num_done_tasks = len(done_tasks)

    # Display the result
    print(f"Employee {employee_name} is done with tasks({num_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")
