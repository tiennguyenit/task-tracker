#!/usr/bin/env python
# coding: utf-8

# In[1]:


# ==================================================
# Program Name: Task Manager
# Author: Tien Nguyen
# Description: A simple command-line task manager
# using lists and dictionaries.
# ==================================================

# Global list that stores all task dictionaries.
tasks = []


def add_task(name, priority, estimated_time):
    """
    Creates a task dictionary and adds it to the tasks list.

    Args:
        name (str): Task name.
        priority (str): Task priority.
        estimated_time (int): Estimated completion time in minutes.

    Returns:
        None
    """

    task = {
        "name": name,
        "priority": priority,
        "is_complete": False,
        "estimated_time": estimated_time
    }

    tasks.append(task)
    print("Task added:", name)


def view_tasks():
    """
    Displays all tasks in the task list.

    Returns:
        None
    """

    if len(tasks) == 0:
        print("No tasks found.")
        return

    print("========== TASK LIST ==========")

    for i, task in enumerate(tasks):

        if task["is_complete"]:
            status = "Completed"
        else:
            status = "Pending"

        print(
            f"{i + 1}. "
            f"{task['name']} | "
            f"Priority: {task['priority']} | "
            f"Status: {status} | "
            f"Estimated Time: {task['estimated_time']} mins"
        )


def complete_task(index):
    """
    Marks a task as completed.

    Args:
        index (int): Zero-based task index.

    Returns:
        None
    """

    if index < 0 or index >= len(tasks):
        print("Invalid task number.")
        return

    tasks[index]["is_complete"] = True

    print("Task marked complete:", tasks[index]["name"])


def delete_task(index):
    """
    Deletes a task from the task list.

    Args:
        index (int): Zero-based task index.

    Returns:
        None
    """

    if index < 0 or index >= len(tasks):
        print("Invalid task number.")
        return

    removed_task = tasks.pop(index)

    print("Task deleted:", removed_task["name"])


def run_manager():
    """
    Main loop of the Task Manager.

    Returns:
        None
    """

    print("Welcome to the Task Manager!")
    print()

    while True:

        print("Options: add | view | complete | delete | quit")

        choice = input("Choose an option: ").strip().lower()

        print()

        if choice == "add":

            name = input("Task name: ")

            if len(name) <= 0:
                print("Task name cannot be empty.")
                print()
                continue

            priority = input("Priority (high, medium, low): ")

            estimated_time = int(
                input("Estimated time in minutes: ")
            )

            add_task(name, priority, estimated_time)

        elif choice == "view":

            view_tasks()

        elif choice == "complete":

            view_tasks()

            if len(tasks) > 0:

                index = int(
                    input("Enter task number to mark complete: ")
                ) - 1

                complete_task(index)

        elif choice == "delete":

            view_tasks()

            if len(tasks) > 0:

                index = int(
                    input("Enter task number to delete: ")
                ) - 1

                delete_task(index)

        elif choice == "quit":

            print("Goodbye!")

            break

        else:

            print(
                "Option not recognized. "
                "Please choose add, view, complete, delete, or quit."
            )

        print()


run_manager()


# In[ ]:




