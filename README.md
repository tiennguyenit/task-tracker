# Task Tracker

**Author:** Tien Nguyen

## Description

Task Tracker is a Python command-line application for creating and managing tasks. The project demonstrates object-oriented programming concepts including encapsulation, inheritance, polymorphism, JSON file persistence, exception handling, and unit testing. Users can create normal, urgent, and recurring tasks, save them to a JSON file, and reload them when the program starts.

---

# How to Run

## 1. Clone the repository

```bash
git clone https://github.com/your-username/task-tracker.git
```

## 2. Open the project folder

```bash
cd task-tracker
```

## 3. Run the Task Manager

```bash
python3 task_manager.py
```

## 4. Run the unit tests

```bash
python3 -m unittest test_task.py -v
```

---

# Features

- Add normal tasks
- Add urgent tasks with deadlines
- Add recurring tasks with frequencies
- View all tasks
- Mark tasks as completed
- Delete tasks
- Set task priorities (high, medium, low)
- Track estimated completion time
- Save tasks to JSON
- Load tasks from JSON
- Supports inheritance and polymorphism
- Includes unit tests using Python's unittest module

---

# Technologies Used

- Python 3
- JSON
- Git
- GitHub
- Visual Studio Code

---

# Project Structure

| File | Description |
|------|-------------|
| `README.md` | Project overview and documentation. |
| `task.py` | Contains the `Task`, `UrgentTask`, and `RecurringTask` classes plus the `task_from_dict()` factory function. |
| `task_manager.py` | Main command-line Task Manager application. |
| `test_task.py` | Unit tests for all task classes. |
| `tasks.json` | Stores task data between program runs. |
| `code_review.md` | Self-review and release readiness checklist. |
| `bug_report.md` | Documents known bugs. |
| `data_model.md` | Describes the Task Manager data model. |
| `test_results.txt` | Output showing all unit tests passed successfully. |
| `task_input.py` | Week 1 practice for collecting task information. |
| `task_input111.py` | Additional Week 1 practice program. |
| `task_priority.py` | Priority validation practice. |
| `task_tracker.py` | Function-based Task Tracker implementation. |
| `task_tracker_exercise.py` | Week 1 function exercises. |
| `test_cases.md` | Test cases created during earlier development. |

---

# Known Bugs and Limitations

- Priority validation is case-sensitive. Entering `High` or `LOW` is rejected instead of automatically converting to lowercase.
- Negative estimated time values are accepted and should be validated before creating a task.

---

# Future Improvements

- Add task editing functionality.
- Add sorting and filtering by priority or completion status.
- Validate negative estimated time input.
- Add due dates for normal tasks.
- Build a graphical user interface (GUI).
- Support searching tasks by keyword.

---

# Week 2 Summary

During Week 2, the project evolved from a simple task list into a complete object-oriented application. File persistence was implemented using JSON, inheritance was introduced through `UrgentTask` and `RecurringTask`, polymorphism allowed multiple task types to be managed together, and unit tests were added to verify that the application behaves correctly.