# Code Review

## Code Quality

- [x] All functions and methods have docstrings.
- [x] No unused variables or commented-out code remain.
- [x] Variable and function names are descriptive and follow Python naming conventions.

---

## Correctness

- [x] Adding a task creates the correct object type and appends it to the task list.
- [x] Viewing tasks displays all task information including status.
- [x] Completing a task correctly updates the completion status.
- [x] Deleting a task removes it from the task list and prints the correct task name.
- [x] Saving creates a valid `tasks.json` file.
- [x] Loading restores `Task`, `UrgentTask`, and `RecurringTask` objects correctly using `task_from_dict()`.

---

## Edge Cases

- [x] Empty task lists are handled correctly in `view_tasks()`.
- [x] Invalid priority values are rejected by `set_priority()`.
- [x] Invalid estimated time input is handled using `ValueError`.
- [x] Invalid task numbers are handled in `complete_task()` and `delete_task()`.

---

## Documentation

- [x] README contains all required sections.
- [x] Project Structure lists every project file.
- [x] Known bugs are documented.

---

## Improvement I Made

During the self-review I improved the JSON loading process by adding the `task_from_dict()` factory function. This allows the program to correctly recreate `Task`, `UrgentTask`, and `RecurringTask` objects from the saved JSON file instead of always creating normal `Task` objects.

---

# Release Readiness Checklist: Task Manager v1.0

## Code Quality

- [x] All functions and methods have docstrings
- [x] No unused variables or commented-out code blocks remain
- [x] Variable and function names are descriptive

## Testing

- [x] All unit tests pass with zero failures
- [x] Edge cases are covered in tests
- [x] All three task types have been manually tested end to end

## Documentation

- [x] README is complete and up to date
- [x] Project Structure section lists all files
- [x] Known bugs are documented in bug_report.md
- [x] Future improvements are listed

## Version Control

- [x] All changes committed with clear messages
- [x] Repository is public and accessible

## File Persistence

- [x] tasks.json is generated correctly on save
- [x] Tasks reload correctly on restart for all three task types