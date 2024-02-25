import unittest
from src.classes.queue import Queue

class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_add(self):
        self.queue.add(1)
        self.queue.add(2)
        self.queue.add(3)
        self.assertEqual(self.queue.size(), 3)

    def test_remove(self):
        self.queue.add(1)
        self.queue.add(2)
        self.queue.add(3)
        self.assertEqual(self.queue.remove(), 1)
        self.assertEqual(self.queue.remove(), 2)
        self.assertEqual(self.queue.remove(), 3)
        self.assertEqual(self.queue.size(), 0)

    def test_size(self):
        self.queue.add(1)
        self.queue.add(2)
        self.queue.add(3)
        self.assertEqual(self.queue.size(), 3)

    def test_to_list(self):
        self.queue.add(1)
        self.queue.add(2)
        self.queue.add(3)
        self.assertEqual(self.queue.to_list(), [1, 2, 3])

    def test_remove_from_empty_queue(self):
        with self.assertRaises(IndexError):
            self.queue.remove()

    def test_copy(self):
        self.queue.add(1)
        self.queue.add(2)
        self.queue.add(3)
        new_queue = self.queue.copy()
        self.assertEqual(new_queue.to_list(), [1, 2, 3])
        self.assertNotEqual(new_queue, self.queue)

    def test_to_string(self):
        self.queue.add(1)
        self.queue.add(2)
        self.queue.add(3)
        self.assertEqual(str(self.queue), "deque([1, 2, 3])")