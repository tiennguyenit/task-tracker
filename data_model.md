# Data Model

## Section 1 – Task Object Structure

| Field Name | Data Type | Description | Default Value |
|------------|-----------|-------------|---------------|
| name | str | Name of the task | User input |
| priority | str | Priority level (high, medium, low) | User input |
| is_complete | bool | Indicates whether the task is completed | False |
| estimated_time | int | Estimated time to complete the task in minutes | User input |

## Section 1 – Task Object Structure

| Attribute | Data Type | Description | Default Value |
|-----------|-----------|-------------|---------------|
| name | str | Name of the task | User input |
| priority | str | Priority level (high, medium, low) | User input |
| is_complete | bool | Indicates whether task is completed | False |
| estimated_time | int | Estimated completion time in minutes | User input |

---

## Section 2 – Requirements Mapping

| Functional Requirement | Data Field or Function | How It Is Fulfilled |
|------------------------|------------------------|---------------------|
| Add a task | add_task() | Creates a dictionary and appends it to the tasks list |
| View tasks | view_tasks() | Displays every task in the list |
| Complete a task | complete_task() | Updates is_complete to True |
| Delete a task | delete_task() | Removes a task using pop() |

---

## Section 3 – Assumptions

- Tasks are stored only in memory while the program is running.
- Estimated time is entered as a whole number of minutes.
- Priority should be high, medium, or low.
- Each task starts with is_complete set to False.

---

## Week 2 Day 3 Update: OOP Refactor

The Task Manager was refactored from using dictionaries to using a Task class. Instead of storing task information in plain dictionaries, each task is now represented as a Task object that contains both data and behavior.

Encapsulation protects important data such as the priority and completion status by making them private attributes. This ensures that changes are made only through controlled methods like `set_priority()` and `mark_complete()`.

The `to_dict()` and `from_dict()` methods are required because JSON can only store basic data types such as dictionaries, lists, strings, numbers, and booleans. These methods convert between Task objects and dictionaries when saving and loading tasks.