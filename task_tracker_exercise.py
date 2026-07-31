#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Program: Task Tracker
# Author: Tien Nguyen
# Description: Display a welcome message.

print("=============================")
print("      TASK TRACKER")
print("=============================")
print("Welcome to Task Tracker")
print("Student: Tien Nguyen")
print("Date: 29-07-2026")


# In[2]:


# Exercise 2 - Create a task
task_id = 101
task_name = "Design Home Page"
priority = "High"

print("Task ID:", task_id)
print("Task Name:", task_name)
print("Priority:", priority)


# In[3]:


# Exercise 3 - Display Data types
task_name = "Design Payment page"
task_id = 201
estimated_hours = 7.5
task_completed = False

print("Task Name:", task_name)
print(type(task_name))

print("Task ID:", task_id)
print(type(task_id))

print("Estimated Hours:", estimated_hours)
print(type(estimated_hours))

print("Task Completed:", task_completed)
print(type(task_completed))


# In[4]:


# Exercise 4 - Employee task assignment
employee_name = input("Enter Employee Name: ")
task_name = input("Enter Task Name: ")

print()
print("Employee:", employee_name)
print("Assigned Task:", task_name)


# In[5]:


# Exercise 5 - Task information form
task_id = input("Enter Task ID: ")
task_name = input("Enter Task Name: ")
department = input("Enter Department: ")
estimated_hours = input("Enter Estimated Hours: ")

print("=========================")
print("TASK INFORMATION")
print("=========================")
print("Task ID:", task_id)
print("Task Name:", task_name)
print("Department:", department)
print("Estimated Hours:", estimated_hours)


# In[6]:


# Exercise 6 - Daily work log
employee_name = "Hangsam"
tasks_completed = 15
working_hours = 40.5
attendance = True

print("Employee:", employee_name)
print("Tasks Completed:", tasks_completed)
print("Working Hours:", working_hours)
print("Attendance:", attendance)


# In[7]:


# Exercise 7 - Project Registration
project_name = input("Project Name: ")
team_leader = input("Team Leader: ")
team_members = int(input("Number of Team Members: "))

print()
print("Project Name:", project_name)
print("Team Leader:", team_leader)
print("Team Members:", team_members)


# In[9]:


# Exercise 8 - Task summary report
task_name = "Launching First Smart Aircraft to Space"
assigned_employee = "Thomas"
priority = "Medium"
due_date = "30-07-2026"
status = "Pending"

print("==========================")
print("TASK SUMMARY")
print("==========================")
print("Task Name:", task_name)
print("Assigned To:", assigned_employee)
print("Priority:", priority)
print("Due Date:", due_date)
print("Status:", status)


# In[10]:


# Exercise 9 - User input and Data types
task_id = int(input("Enter Task ID: "))
estimated_hours = float(input("Enter Estimated Hours: "))

print("Task ID:", task_id)
print(type(task_id))

print("Estimated Hours:", estimated_hours)
print(type(estimated_hours))


# In[11]:


# Exercise 10 - Mini Task Tracker Registration
print("====================================")
print("      TASK TRACKER REPORT")
print("====================================")

task_id = int(input("Task ID: "))
task_name = input("Task Name: ")
employee_name = input("Employee Name: ")
department = input("Department: ")
priority = input("Priority: ")
estimated_hours = float(input("Estimated Hours: "))
completed = input("Completed (True/False): ")

print()

print("====================================")
print("      TASK TRACKER REPORT")
print("====================================")
print("Task ID:", task_id)
print("Task Name:", task_name)
print("Employee Name:", employee_name)
print("Department:", department)
print("Priority:", priority)
print("Estimated Hours:", estimated_hours)
print("Completed:", completed)
print("====================================")


# In[12]:


# Bonus Challenge - Create student task tracker
print("========================================")
print("     STUDENT TASK TRACKER REPORT")
print("========================================")

student_id = input("Student ID: ")
student_name = input("Student Name: ")
course = input("Course: ")
assignment_name = input("Assignment Name: ")
assignment_deadline = input("Assignment Deadline: ")
estimated_time = float(input("Estimated Time (Hours): "))
assignment_submitted = input("Assignment Submitted (True/False): ")

print()

print("========================================")
print("     STUDENT TASK TRACKER REPORT")
print("========================================")
print("Student ID:", student_id)
print("Student Name:", student_name)
print("Course:", course)
print("Assignment Name:", assignment_name)
print("Assignment Deadline:", assignment_deadline)
print("Estimated Time:", estimated_time)
print("Assignment Submitted:", assignment_submitted)
print("========================================")


# In[13]:


# All in one
# ==========================================================
# Program Name: Student Project Planner
# Author: Tien Nguyen
# Description: Collects project information and displays
#              a professional project report.
# ==========================================================

print("========================================================")
print("            STUDENT PROJECT PLANNER")
print("========================================================")
print()

# -----------------------------
# Student Information
# -----------------------------
student_name = input("Enter Student Name: ")
student_id = input("Enter Student ID: ")
course = input("Enter Course: ")
university = input("Enter University: ")

print()

# -----------------------------
# Project Information
# -----------------------------
project_name = input("Enter Project Name: ")
project_purpose = input("Enter Project Purpose: ")
project_description = input("Enter Project Description: ")

print()

# -----------------------------
# Team Information
# -----------------------------
team_leader = input("Enter Team Leader: ")
number_of_teammates = int(input("Enter Number of Team Members: "))
team_members = input("Enter Team Members (separate names with commas): ")

print()

# -----------------------------
# Task Information
# -----------------------------
task_name = input("Enter Task Name: ")
task_description = input("Enter Task Description: ")
task_priority = input("Enter Task Priority (High/Medium/Low): ")
task_deadline = input("Enter Task Deadline: ")

task_duration = int(input("Enter Task Duration (days): "))
days_used = int(input("Enter Number of Days Used: "))

days_remaining = task_duration - days_used

print()

# -----------------------------
# Progress Information
# -----------------------------
completion_percentage = float(input("Enter Completion Percentage (%): "))
motivation = input("Enter Your Motivation: ")
completed = input("Is the Task Completed? (True/False): ")

print()

# ==========================================================
# REPORT
# ==========================================================

print("========================================================")
print("               STUDENT PROJECT REPORT")
print("========================================================")

print()
print("STUDENT INFORMATION")
print("------------------------------")
print("Student Name          :", student_name)
print("Student ID            :", student_id)
print("Course                :", course)
print("University            :", university)

print()
print("PROJECT INFORMATION")
print("------------------------------")
print("Project Name          :", project_name)
print("Project Purpose       :", project_purpose)
print("Project Description   :", project_description)

print()
print("TEAM INFORMATION")
print("------------------------------")
print("Team Leader           :", team_leader)
print("Number of Members     :", number_of_teammates)
print("Team Members          :", team_members)

print()
print("TASK INFORMATION")
print("------------------------------")
print("Task Name             :", task_name)
print("Task Description      :", task_description)
print("Priority              :", task_priority)
print("Task Deadline         :", task_deadline)
print("Task Duration         :", task_duration, "days")
print("Days Used             :", days_used, "days")
print("Days Remaining        :", days_remaining, "days")

print()
print("PROJECT STATUS")
print("------------------------------")
print("Completion            :", completion_percentage, "%")
print("Motivation            :", motivation)
print("Completed             :", completed)

print()
print("========================================================")
print("Thank you for using Student Project Planner!")
print("========================================================")


# In[ ]:




