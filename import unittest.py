import unittest
from Lab6 import read_tasks, create_queue, is_empty
class TestTaskQueue(unittest.TestCase):

    def test_read_tasks(self):
        tasks = read_tasks("test_tasks.txt")
        expected_tasks = [('Task 1', 1), ('Task 2', 2), ('Task 3', 3)]
        self.assertEqual(tasks, expected_tasks)

    def test_create_queue(self):
        tasks = [('Task 1', 1), ('Task 2', 2), ('Task 3', 3)]
        queue = create_queue(tasks)
        expected_queue = [('Task 3', 3), ('Task 2', 2), ('Task 1', 1)]
        self.assertEqual(queue, expected_queue)

    def test_is_empty(self):
        queue = []
        self.assertTrue(is_empty(queue))

        queue = [('Task 1', 1)]
        self.assertFalse(is_empty(queue))

if __name__ == '__main__':
    unittest.main()
