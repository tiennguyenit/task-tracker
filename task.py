class Task:
    """
    Represents a single task.
    """

    def __init__(self, name, priority, estimated_time):
        """
        Initializes a new Task.

        Args:
            name (str): Task name.
            priority (str): Task priority.
            estimated_time (int): Estimated completion time.
        """

        self.name = name
        self.__priority = priority
        self.estimated_time = estimated_time
        self.__is_complete = False

    def get_priority(self):
        """
        Returns the task priority.
        """
        return self.__priority

    def set_priority(self, priority):
        """
        Updates the priority if it is valid.
        """

        if priority in ["high", "medium", "low"]:
            self.__priority = priority
        else:
            print("Invalid priority. Choose high, medium, or low.")

    def get_is_complete(self):
        """
        Returns the completion status.
        """

        return self.__is_complete

    def mark_complete(self):
        """
        Marks the task as completed.
        """

        self.__is_complete = True

    def to_dict(self):
        """
        Converts this object into a dictionary.
        """

        return {
            "name": self.name,
            "priority": self.__priority,
            "estimated_time": self.estimated_time,
            "is_complete": self.__is_complete
        }

    @classmethod
    def from_dict(cls, data):
        """
        Creates a Task object from a dictionary.
        """

        task = cls(
            data["name"],
            data["priority"],
            data["estimated_time"]
        )

        if data["is_complete"]:
            task.mark_complete()

        return task

    def __str__(self):
        """
        Returns a readable string.
        """

        status = "Done" if self.__is_complete else "Pending"

        return (
            f"{self.name} | "
            f"Priority: {self.__priority} | "
            f"Status: {status} | "
            f"Est. Time: {self.estimated_time} mins"
        )