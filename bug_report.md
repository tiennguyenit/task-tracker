# Bug Report

## BUG-01

**Description:** The program accepts negative or zero estimated time values when creating a task.

**Steps to Reproduce:**
1. Run `task_manager.py`.
2. Choose `add`, `add-urgent`, or `add-recurring`.
3. Enter `-10` or `0` for the estimated time.

**Expected Behavior:**  
The program should reject zero or negative values and ask the user to enter a positive number.

**Actual Behavior:**  
The task is created successfully with an invalid estimated time.

---

## BUG-02

**Description:** Empty task names are accepted for urgent and recurring tasks.

**Steps to Reproduce:**
1. Run `task_manager.py`.
2. Choose `add-urgent` or `add-recurring`.
3. Press **Enter** without typing a task name.
4. Complete the remaining prompts.

**Expected Behavior:**  
The program should display an error message and require the user to enter a non-empty task name.

**Actual Behavior:**  
The task is added with an empty name.