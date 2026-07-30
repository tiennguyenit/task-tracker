# Task Tracker Priority Checker - Test Cases

| Test Case ID | Description | Input | Expected Output |
|---|---|---|---|
| TC-01 | Test a high priority task | Task: Finish an assignment, Priority: high | Urgent: Handle this task first. |
| TC-02 | Test a medium priority task | Task: Buy groceries, Priority: medium | Important: Schedule this task soon. |
| TC-03 | Test an empty task name edge case | Task: empty, Priority: high | Task name cannot be empty. |
| TC-04 | Test an invalid priority value | Task: Create a report, Priority: urgent | Priority not recognized. Please enter high, medium, or low. |
| TC-05 | Test quitting the program | Task: quit | Session ended. Goodbye! |