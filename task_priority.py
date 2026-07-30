#!/usr/bin/env python
# coding: utf-8

# In[2]:


# ==================================================
# Program Name: Task Tracker Priority Checker
# Author: Tien Nguyen
# Description: Allows users to enter tasks and checks
#              their priority level using conditions.
# ==================================================


print("Welcome to Task Tracker Priority Checker!")
print()


task_name = ""

# The loop continues running until the user enters "quit"
while task_name != "quit":

    task_name = input("Enter a task name (or type 'quit' to stop): ")

    # Check that the user did not choose to quit
    if task_name != "quit":

        # Comparison operator != checks if task name is valid
        if len(task_name) > 0:
            priority = input("Enter priority (high, medium, low): ")

            if priority == "high":
                print("Urgent: Handle this task first.")

            elif priority == "medium":
                print("Important: Schedule this task soon.")

            elif priority == "low":
                print("Low priority: Handle when time allows.")

            else:
                print(
                    "Priority not recognized. "
                    "Please enter high, medium, or low."
                )

        else:
            print("Task name cannot be empty.")

        print()


print("Session ended. Goodbye!")


# In[ ]:




