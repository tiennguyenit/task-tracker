#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Week 2 Day 1

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


# In[8]:


# Week 2 Day 2

# ==================================================
# Program Name: Task Manager
# Author: Tien Nguyen
# Description: A simple command-line task manager
# using lists and dictionaries.
# ==================================================

# Step 1 & 2: Create json file >>>>>
import json

# Constant representing the file used to store tasks
TASKS_FILE = "tasks.json"
# <<<<< End step 1 & 2


# Global list that stores all task dictionaries.
tasks = []

# Step 3: Write the save_tasks() function >>>>>
def save_tasks():
    """
    Saves the current tasks list into a JSON file.

    Returns:
        None
    """

    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

    print("Tasks saved.")
# <<<<< End step 3

# Step 4: Write the load_tasks() function >>>>>
def load_tasks():
    """
    Loads tasks from the JSON file into the global tasks list.

    If the file does not exist or is corrupted,
    an empty task list will be created.

    Returns:
        None
    """

    global tasks

    try:
        with open(TASKS_FILE, "r") as file:
            tasks = json.load(file)

        print(f"Loaded {len(tasks)} task(s).")


    except FileNotFoundError:

        tasks = []

        print(
            "No saved file found. "
            "Starting with an empty task list."
        )


    except json.JSONDecodeError:

        tasks = []

        print(
            "Save file is corrupted. "
            "Starting with an empty task list."
        )
# <<<<< End step 4

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

    Loads saved tasks, handles user commands,
    and saves tasks before exiting.

    Returns:
        None
    """

# Part 2 & 3: Add error handling and call load, and save tasks >>>>>
    # Add load_tasks() function >>>>>
    load_tasks()
    # <<<<< End add

    print("Welcome to the Task Manager!")
    print()

    while True:
        # Added the save option
        print("Options: add | view | complete | delete | save | quit")

        choice = input("Choose an option: ").strip().lower()

        print()

        if choice == "add":

            name = input("Task name: ")

            if len(name) <= 0:
                print("Task name cannot be empty.")
                print()
                continue

            priority = input("Priority (high, medium, low): ")

            # Added exception handling >>>>>
        #   estimated_time = int(
        #       input("Estimated time in minutes: ")
        #   )
            try:

                estimated_time = int(
                    input(
                        "Estimated time in minutes: "
                    )
                )


            except ValueError:

                print(
                    "Please enter a whole number for estimated time."
                )

                print()

                continue


            add_task(name, priority, estimated_time)


        elif choice == "view":

            view_tasks()


        elif choice == "complete":

            view_tasks()
      #      if len(tasks) > 0:
      #         index = int(
      #             input("Enter task number to mark complete: ")
      #          ) - 1

      #          complete_task(index)

        # Add exception for completed tasks >>>>>

            try:

                index = int(
                    input(
                        "Enter task number to mark complete: "
                    )
                ) - 1


                complete_task(index)


            except ValueError:

                print(
                    "Please enter a valid task number."
                ) 


        elif choice == "delete":

            view_tasks()
        #    if len(tasks) > 0:

        #        index = int(
        #            input("Enter task number to delete: ")
        #        ) - 1

        #        delete_task(index)

            # Add exception for deleted tasks
            try:

                index = int(
                    input(
                        "Enter task number to delete: "
                    )
                ) - 1


                delete_task(index)


            except ValueError:

                print(
                    "Please enter a valid task number."
                )


        # Add save condition
        elif choice == "save":

            save_tasks()


        # Save tasks after quit the program
        elif choice == "quit":

            save_tasks()

            print("Goodbye!")

            break


        else:

            print(
                "Option not recognized. "
                "Please choose add, view, complete, delete, save, or quit."
            )

        print()


run_manager()


# In[4]:


# Week 2 Day 3

# ==================================================
# Program: Task Manager
# Author: Tien Nguyen
# Description:
# A command-line Task Manager that uses a Task class,
# JSON file persistence, and error handling.
# ==================================================

import json
from task import Task

# Constant representing the JSON file used to save tasks
TASKS_FILE = "tasks.json"

# Global list that stores all Task objects
tasks = []


def save_tasks():
    """
    Saves all tasks to a JSON file.
    """

    with open(TASKS_FILE, "w") as file:
        json.dump(
            [task.to_dict() for task in tasks],
            file,
            indent=4
        )

    print("Tasks saved.")


def load_tasks():
    """
    Loads tasks from the JSON file.

    If the file does not exist or is corrupted,
    an empty task list is created.
    """

    global tasks

    try:
        with open(TASKS_FILE, "r") as file:
            tasks = [
                Task.from_dict(task)
                for task in json.load(file)
            ]

        print(f"Loaded {len(tasks)} task(s).")

    except FileNotFoundError:
        tasks = []
        print("No saved file found. Starting with an empty task list.")

    except json.JSONDecodeError:
        tasks = []
        print("Save file is corrupted. Starting with an empty task list.")


def add_task(name, priority, estimated_time):
    """
    Creates a Task object and adds it to the tasks list.

    Args:
        name (str): Task name.
        priority (str): Task priority.
        estimated_time (int): Estimated completion time.

    Returns:
        None
    """

    task = Task(name, priority, estimated_time)

    tasks.append(task)

    print("Task added:", name)


def view_tasks():
    """
    Displays all tasks.

    Returns:
        None
    """

    if len(tasks) == 0:
        print("No tasks found.")
        return

    print("========== TASK LIST ==========")

    for index, task in enumerate(tasks):
        print(f"{index + 1}. {task}")

    print("===============================")

def complete_task(index):
    """
    Marks a task as completed.

    Args:
        index (int): Zero-based index of the task.

    Returns:
        None
    """

    if index < 0 or index >= len(tasks):
        print("Invalid task number.")
        return

    tasks[index].mark_complete()

    print("Task marked complete:", tasks[index].name)


def delete_task(index):
    """
    Deletes a task from the task list.

    Args:
        index (int): Zero-based index of the task.

    Returns:
        None
    """

    if index < 0 or index >= len(tasks):
        print("Invalid task number.")
        return

    removed = tasks.pop(index)

    print("Task deleted:", removed.name)


def run_manager():
    """
    Main loop for the Task Manager.

    Loads saved tasks, accepts user commands,
    performs task operations, and saves tasks
    before exiting.
    """

    load_tasks()

    print()
    print("Welcome to the Task Manager!")
    print()

    while True:

        print("Options: add | view | complete | delete | save | quit")

        choice = input("Choose an option: ").strip().lower()

        print()

        if choice == "add":

            name = input("Task name: ").strip()

            if len(name) == 0:
                print("Task name cannot be empty.")
                print()
                continue

            priority = input(
                "Priority (high, medium, low): "
            ).strip().lower()

            try:
                estimated_time = int(
                    input("Estimated time in minutes: ")
                )

            except ValueError:
                print("Please enter a whole number for estimated time.")
                print()
                continue

            add_task(
                name,
                priority,
                estimated_time
            )

        elif choice == "view":

            view_tasks()

        elif choice == "complete":

            if len(tasks) == 0:
                print("No tasks available.")
                print()
                continue

            view_tasks()

            try:

                index = int(
                    input("Enter task number to mark complete: ")
                ) - 1

                complete_task(index)

            except ValueError:

                print("Please enter a valid task number.")

        elif choice == "delete":

            if len(tasks) == 0:
                print("No tasks available.")
                print()
                continue

            view_tasks()

            try:

                index = int(
                    input("Enter task number to delete: ")
                ) - 1

                delete_task(index)

            except ValueError:

                print("Please enter a valid task number.")

        elif choice == "save":

            save_tasks()

        elif choice == "quit":

            save_tasks()

            print("Goodbye!")

            break

        else:

            print(
                "Option not recognized."
            )
            print(
                "Please choose add, view, complete, delete, save, or quit."
            )

        print()


run_manager()


# In[3]:


# Week 2 Day 4

# ==================================================
# Program: Task Manager
# Author: Tien Nguyen
# Description:
# A command-line Task Manager that uses a Task class,
# JSON file persistence, and error handling.
# ==================================================

import json

from task import (
    Task,
    UrgentTask,
    RecurringTask,
    task_from_dict
)


TASKS_FILE = "tasks.json"


tasks = []



def save_tasks():
    """
    Saves all tasks to JSON file.
    """

    with open(TASKS_FILE, "w") as file:

        json.dump(
            [
                task.to_dict()
                for task in tasks
            ],
            file,
            indent=4
        )


    print("Tasks saved.")



def load_tasks():
    """
    Loads tasks from JSON file.
    """

    global tasks


    try:

        with open(TASKS_FILE, "r") as file:

            tasks = [
                task_from_dict(task)
                for task in json.load(file)
            ]


        print(
            f"Loaded {len(tasks)} task(s)."
        )


    except FileNotFoundError:

        tasks = []

        print(
            "No saved file found. Starting empty."
        )


    except json.JSONDecodeError:

        tasks = []

        print(
            "Save file corrupted."
        )



def add_task(name, priority, estimated_time):
    """
    Adds normal task.
    """

    task = Task(
        name,
        priority,
        estimated_time
    )

    tasks.append(task)

    print(
        "Task added:",
        name
    )



def add_urgent_task():
    """
    Adds urgent task.
    """

    name = input(
        "Task name: "
    ).strip()


    try:

        estimated_time = int(
            input(
                "Estimated time in minutes: "
            )
        )


    except ValueError:

        print(
            "Invalid estimated time."
        )

        return


    deadline = input(
        "Deadline: "
    ).strip()


    task = UrgentTask(
        name,
        estimated_time,
        deadline
    )


    tasks.append(task)


    print(
        "Urgent task added:",
        name
    )



def add_recurring_task():
    """
    Adds recurring task.
    """

    name = input(
        "Task name: "
    ).strip()


    priority = input(
        "Priority (high, medium, low): "
    ).strip().lower()


    try:

        estimated_time = int(
            input(
                "Estimated time in minutes: "
            )
        )


    except ValueError:

        print(
            "Invalid estimated time."
        )

        return


    frequency = input(
        "Frequency: "
    ).strip()


    task = RecurringTask(
        name,
        priority,
        estimated_time,
        frequency
    )


    tasks.append(task)


    print(
        "Recurring task added:",
        name
    )



def view_tasks():
    """
    Displays all tasks.
    """

    if len(tasks) == 0:

        print(
            "No tasks found."
        )

        return


    print(
        "========== TASK LIST =========="
    )


    for index, task in enumerate(tasks):

        print(
            f"{index + 1}. {task}"
        )


    print(
        "==============================="
    )



def complete_task(index):
    """
    Completes task.
    """

    if index < 0 or index >= len(tasks):

        print(
            "Invalid task number."
        )

        return


    tasks[index].mark_complete()


    print(
        "Task completed:",
        tasks[index].name
    )



def delete_task(index):
    """
    Deletes task.
    """

    if index < 0 or index >= len(tasks):

        print(
            "Invalid task number."
        )

        return


    removed = tasks.pop(index)


    print(
        "Task deleted:",
        removed.name
    )



def run_manager():
    """
    Main Task Manager loop.
    """

    load_tasks()


    print()
    print(
        "Welcome to the Task Manager!"
    )
    print()


    while True:


        print(
            "Options: add | add-urgent | add-recurring | view | complete | delete | save | quit"
        )


        choice = input(
            "Choose an option: "
        ).strip().lower()

        print()

        if choice == "add":

            name = input(
                "Task name: "
            ).strip()


            priority = input(
                "Priority (high, medium, low): "
            ).strip().lower()


            try:

                estimated_time = int(
                    input(
                        "Estimated time in minutes: "
                    )
                )


            except ValueError:

                print(
                    "Invalid time."
                )

                continue


            add_task(
                name,
                priority,
                estimated_time
            )



        elif choice == "add-urgent":

            add_urgent_task()
            print()


        elif choice == "add-recurring":

            add_recurring_task()
            print()


        elif choice == "view":

            view_tasks()
            print()


        elif choice == "complete":

            view_tasks()


            index = int(
                input(
                    "Enter task number: "
                )
            ) - 1


            complete_task(index)
            print()


        elif choice == "delete":

            view_tasks()


            index = int(
                input(
                    "Enter task number: "
                )
            ) - 1


            delete_task(index)
            print()


        elif choice == "save":

            save_tasks()
            print()


        elif choice == "quit":

            save_tasks()

            print(
                "Goodbye!"
            )

            break



        else:

            print(
                "Option not recognized."
            )
        print()


if __name__ == "__main__":

    run_manager()


# In[ ]:




