import unittest
from src.classes.stack import Stack

class TestStack(unittest.TestCase):
    def setUp(self) -> None:
        self.stack = Stack()

    def test_push(self) -> None:
        self.stack.push("+1")
        self.stack.push("+2")
        self.assertEqual(self.stack.peek(), "+2")
        self.stack.push("+3")
        self.assertEqual(self.stack.peek(), "+3")

    def test_pop(self) -> None:
        self.stack.push("+1")
        self.stack.push("+2")
        self.stack.push("+3")
        self.stack.pop()
        self.assertEqual(self.stack.peek(), "+2")
        self.stack.pop()
        self.assertEqual(self.stack.peek(), "+1")

    def test_peek(self) -> None:
        self.stack.push("+1")
        self.stack.push("+2")
        self.assertEqual(self.stack.peek(), "+2")
        self.stack.push("+3")
        self.assertEqual(self.stack.peek(), "+3")

    def test_is_empty(self) -> None:
        self.assertTrue(self.stack.is_empty())
        self.stack.push("+1")
        self.assertFalse(self.stack.is_empty())

    def test_size(self) -> None:
        self.assertEqual(self.stack.size(), 0)
        self.stack.push("+1")
        self.assertEqual(self.stack.size(), 1)
        self.stack.push("+2")
        self.assertEqual(self.stack.size(), 2)
        self.stack.push("+3")
        self.assertEqual(self.stack.size(), 3)
        self.stack.pop()
        self.assertEqual(self.stack.size(), 2)
        self.stack.pop()
        self.assertEqual(self.stack.size(), 1)
        self.stack.pop()
        self.assertEqual(self.stack.size(), 0)

    def test_pop_from_empy_stack(self) -> None:
        with self.assertRaises(IndexError):
            self.stack.pop()

    def test_peek_from_empy_stack(self) -> None:
        with self.assertRaises(IndexError):
            self.stack.peek()
