import unittest

from task import Task, UrgentTask, RecurringTask


class TestTask(unittest.TestCase):
    """Unit tests for Task class."""

    def setUp(self):
        """Create a fresh Task before each test."""
        self.task = Task("Buy groceries", "high", 30)

    def test_task_creation(self):
        """Test task creation."""
        self.assertEqual(self.task.name, "Buy groceries")
        self.assertEqual(self.task.get_priority(), "high")
        self.assertEqual(self.task.estimated_time, 30)
        self.assertFalse(self.task.get_is_complete())

    def test_mark_complete(self):
        """Test mark_complete()."""
        self.task.mark_complete()
        self.assertTrue(self.task.get_is_complete())

    def test_set_priority_valid(self):
        """Test valid priority update."""
        self.task.set_priority("low")
        self.assertEqual(self.task.get_priority(), "low")

    def test_set_priority_invalid(self):
        """Test invalid priority update."""
        old_priority = self.task.get_priority()
        self.task.set_priority("urgent")
        self.assertEqual(self.task.get_priority(), old_priority)

    def test_to_dict(self):
        """Test to_dict()."""
        data = self.task.to_dict()

        self.assertEqual(data["name"], "Buy groceries")
        self.assertEqual(data["priority"], "high")
        self.assertEqual(data["estimated_time"], 30)
        self.assertFalse(data["is_complete"])

    def test_from_dict(self):
        """Test from_dict()."""
        data = {
            "type": "Task",
            "name": "Buy groceries",
            "priority": "high",
            "estimated_time": 30,
            "is_complete": False
        }

        task = Task.from_dict(data)

        self.assertEqual(task.name, "Buy groceries")
        self.assertEqual(task.get_priority(), "high")
        self.assertEqual(task.estimated_time, 30)
        self.assertFalse(task.get_is_complete())

    def test_str_output(self):
        """Test string output."""
        text = str(self.task)

        self.assertIn("Buy groceries", text)
        self.assertIn("Pending", text)

    def test_task_deletion(self):
        """Test task deletion."""

        tasks = [self.task]

        removed_task = tasks.pop(0)

        self.assertEqual(removed_task.name, "Buy groceries")
        self.assertEqual(len(tasks), 0)


class TestUrgentTask(unittest.TestCase):
    """Unit tests for UrgentTask."""

    def setUp(self):
        """Create a fresh UrgentTask before each test."""
        self.task = UrgentTask(
            "Fix server outage",
            5,
            "2024-12-01"
        )

    def test_urgent_priority_is_always_high(self):
        """Test urgent task priority."""
        self.assertEqual(
            self.task.get_priority(),
            "high"
        )

    def test_urgent_str_contains_label(self):
        """Test urgent label."""
        self.assertIn(
            "[URGENT]",
            str(self.task)
        )

    def test_urgent_str_contains_deadline(self):
        """Test deadline output."""
        self.assertIn(
            "2024-12-01",
            str(self.task)
        )

    def test_urgent_to_dict_includes_type(self):
        """Test urgent to_dict()."""
        data = self.task.to_dict()

        self.assertEqual(
            data["type"],
            "UrgentTask"
        )

        self.assertIn(
            "deadline",
            data
        )


class TestRecurringTask(unittest.TestCase):
    """Unit tests for RecurringTask."""

    def setUp(self):
        """Create a fresh RecurringTask before each test."""
        self.task = RecurringTask(
            "Team standup",
            "medium",
            15,
            "daily"
        )

    def test_recurring_str_contains_label(self):
        """Test recurring label."""
        self.assertIn(
            "[RECURRING",
            str(self.task)
        )

    def test_recurring_to_dict_includes_type(self):
        """Test recurring to_dict()."""
        data = self.task.to_dict()

        self.assertEqual(
            data["type"],
            "RecurringTask"
        )

        self.assertIn(
            "frequency",
            data
        )

    def test_reset(self):
        """Test reset()."""
        self.task.mark_complete()

        self.assertTrue(
            self.task.get_is_complete()
        )

        self.task.reset()

        self.assertFalse(
            self.task.get_is_complete()
        )


if __name__ == "__main__":
    unittest.main()