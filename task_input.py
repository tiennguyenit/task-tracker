# Program Name: Task Tracker
# Author: Tien Nguyen
# Description: This script collects task information from users and displays a task summary.


print("Welcome to Task Tracker!")
print("Please enter your task details below.")
print()


task_name = input("Enter task name: ")

priority = input("Enter priority level (high, medium, low): ")

estimated_time = int(input("Estimated time to complete (in minutes): "))

urgent = input("Is this task urgent? (yes/no): ")


# Placeholder: task completion status, starts as incomplete
is_complete = False


print()

print("Task Summary")

print("Task:", task_name)
print("Priority:", priority)
print("Estimated Time:", estimated_time, "minutes")
print("Urgent:", urgent)
