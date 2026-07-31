#!/usr/bin/env python
# coding: utf-8

# In[8]:


# ==================================================
# Program Name: Task Tracker
# Author: Tien Nguyen
# Description: Task Tracker using functions,
#              docstrings, scope, and parameters.
# ==================================================

# Global variable (can be used by any function)
app_name = "Task Tracker"


def greet_user():
    """
    Displays a welcome message when the program starts.

    Returns:
        None
    """
    print(f"Welcome to {app_name}!")
    print()


def get_task_input():
    """
    Collects a task name from the user.

    Returns:
        str: The task name entered by the user.
    """
    task_name = input("Enter a task name (or type 'quit' to stop): ")

    # Local variable: only exists inside this function
    return task_name


def get_priority_input(default_priority="low"):
    """
    Collects the task priority from the user.

    Args:
        default_priority (str): Default priority if no input is provided.

    Returns:
        str: The priority entered by the user.
    """

    priority = input("Enter priority (high, medium, low): ")

    # If the user presses Enter without typing anything,
    # use the default priority.
    if priority == "":
        priority = default_priority

    return priority


def check_priority(priority="low"):
    """
    Checks the priority level and returns an appropriate message.

    Args:
        priority (str): The priority level of the task.

    Returns:
        str: A message describing how the task should be handled.
    """

    if priority == "high":
        return "Urgent: Handle this task first."

    elif priority == "medium":
        return "Important: Schedule this task soon."

    elif priority == "low":
        return "Low priority: Handle when time allows."

    else:
        return "Priority not recognized. Please enter high, medium, or low."


def run_tracker():
    """
    Runs the Task Tracker application until the user types 'quit'.

    Returns:
        None
    """

    greet_user()

    while True:

        task_name = get_task_input()

        if task_name == "quit":
            break

        # Check that the task name is not empty
        if len(task_name) > 0:

            priority = get_priority_input()

            message = check_priority(priority)

            print(message)
            print()

        else:
            print("Task name cannot be empty.")
            print()

    print("Session ended. Goodbye!")


# Start the program
run_tracker()


# In[ ]:




