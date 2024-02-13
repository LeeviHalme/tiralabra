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

    def test_remove_from_empty_queue(self):
        with self.assertRaises(IndexError):
            self.queue.remove()
