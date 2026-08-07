# ==================================================
# Program: Task Classes
# Description:
# Defines Task parent class and subclasses:
# UrgentTask and RecurringTask.
#
# Demonstrates:
# - Inheritance
# - Method overriding
# - Polymorphism
# - Object serialization with JSON
# ==================================================


class Task:
    """
    Parent class representing a general task.
    """

    def __init__(self, name, priority, estimated_time):
        """
        Initialize a Task object.
        """

        self.name = name

        # Private attribute to protect priority value
        self.__priority = priority

        self.estimated_time = estimated_time

        # Private attribute for completion status
        self.__is_complete = False


    def get_priority(self):
        """
        Access private priority attribute.
        """

        return self.__priority


    def set_priority(self, priority):
        """
        Update priority if valid.
        """

        if priority in ["high", "medium", "low"]:
            self.__priority = priority

        else:
            print("Invalid priority.")


    def get_is_complete(self):
        """
        Return completion status.
        """

        return self.__is_complete


    def mark_complete(self):
        """
        Mark task as completed.
        """

        self.__is_complete = True


    def to_dict(self):
        """
        Convert object into dictionary.

        This allows Task objects to be saved
        into JSON format.
        """

        return {
            "type": "Task",
            "name": self.name,
            "priority": self.__priority,
            "estimated_time": self.estimated_time,
            "is_complete": self.__is_complete
        }


    @classmethod
    def from_dict(cls, data):
        """
        Recreate Task object from dictionary.

        Used when loading tasks from JSON.
        """

        task = cls(
            data["name"],
            data["priority"],
            data["estimated_time"]
        )

        if data.get("is_complete"):
            task.mark_complete()

        return task


    def __str__(self):
        """
        String representation of Task.

        This method is overridden by subclasses.
        """

        status = "Done" if self.__is_complete else "Pending"

        return (
            f"{self.name} | "
            f"Priority: {self.__priority} | "
            f"Status: {status} | "
            f"Est. Time: {self.estimated_time} mins"
        )



# ==================================================
# Inheritance:
# UrgentTask inherits everything from Task.
#
# Difference:
# - Priority is automatically "high"
# - Adds deadline attribute
# - Overrides __str__ and to_dict()
# ==================================================

class UrgentTask(Task):
    """
    Represents a high priority task with deadline.
    """

    def __init__(self, name, estimated_time, deadline):

        # Call parent constructor
        super().__init__(
            name,
            "high",
            estimated_time
        )

        self.deadline = deadline


    def __str__(self):
        """
        Override parent __str__ method.

        Demonstrates polymorphism:
        print(task) behaves differently
        depending on object type.
        """

        status = (
            "Done"
            if self.get_is_complete()
            else "Pending"
        )

        return (
            f"[URGENT] {self.name} | "
            f"Status: {status} | "
            f"Est. Time: {self.estimated_time} mins | "
            f"Deadline: {self.deadline}"
        )


    def to_dict(self):
        """
        Convert UrgentTask into dictionary.

        Calls parent method then adds
        subclass-specific information.
        """

        data = super().to_dict()

        data["type"] = "UrgentTask"
        data["deadline"] = self.deadline

        return data



# ==================================================
# Second subclass.
#
# RecurringTask represents tasks that repeat
# on a schedule.
# ==================================================

class RecurringTask(Task):
    """
    Represents a repeating task.
    """

    def __init__(self, name, priority, estimated_time, frequency):

        # Reuse Task initialization
        super().__init__(
            name,
            priority,
            estimated_time
        )

        self.frequency = frequency


    def __str__(self):
        """
        Override parent string output.
        """

        status = (
            "Done"
            if self.get_is_complete()
            else "Pending"
        )

        return (
            f"[RECURRING: {self.frequency}] "
            f"{self.name} | "
            f"Priority: {self.get_priority()} | "
            f"Status: {status} | "
            f"Est. Time: {self.estimated_time} mins"
        )


    def reset(self):
        """
        Reset recurring task for next cycle.

        Uses name-mangled private variable
        from parent class.
        """

        self._Task__is_complete = False

        print(
            f"Task reset for next {self.frequency}: {self.name}"
        )


    def to_dict(self):
        """
        Convert RecurringTask into dictionary.
        """

        data = super().to_dict()

        data["type"] = "RecurringTask"
        data["frequency"] = self.frequency

        return data



# ==================================================
# Factory Function
#
# Purpose:/
# Decide which object should be createdd
# when loading JSON data.
# ==================================================

def task_from_dict(data):
    """
    Creates correct Task object based on type.
    """

    task_type = data.get("type", "Task")


    if task_type == "UrgentTask":

        task = UrgentTask(
            data["name"],
            data["estimated_time"],
            data["deadline"]
        )


    elif task_type == "RecurringTask":

        task = RecurringTask(
            data["name"],
            data["priority"],
            data["estimated_time"],
            data["frequency"]
        )


    else:

        task = Task.from_dict(data)


    if data.get("is_complete"):
        task.mark_complete()


    return task



# ==================================================
# Polymorphism Demonstration
#
# All objects are stored in the same list.
# The loop calls the same method:
# print(task)
#
# Each object provides different output.
# ==================================================

if __name__ == "__main__":

    demo_tasks = [

        Task(
            "Buy groceries",
            "low",
            30
        ),

        UrgentTask(
            "Fix server outage",
            5,
            "2024-12-01"
        ),

        RecurringTask(
            "Team standup",
            "medium",
            15,
            "daily"
        )
    ]


    print("--- Polymorphism Demo ---")


    for task in demo_tasks:

        print(task)

        print(
            "Is a Task instance:",
            isinstance(task, Task)
        )

        print()