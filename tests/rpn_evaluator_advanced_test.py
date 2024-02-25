import unittest
from collections import deque
from src.classes.queue import Queue
from src.classes.rpn_evaluator import RPNEvaluator
from src.classes.exceptions import MalformedExpressionException

class TestAdvancedRPNEvaluator(unittest.TestCase):
    def setUp(self) -> None:
        self.rpn = RPNEvaluator()

    def test_division_by_zero(self):
        with self.assertRaises(MalformedExpressionException):
            self.rpn.evaluate(Queue(deque(["5", "0", "/"])))

    def too_few_operands(self):
        with self.assertRaises(MalformedExpressionException):
            self.rpn.evaluate(Queue(deque(["5", "*"])))

    def test_too_many_operands(self):
        with self.assertRaises(MalformedExpressionException):
            self.rpn.evaluate(Queue(deque(["5", "6", "+", "7"])))

    def test_invalid_operator(self):
        with self.assertRaises(MalformedExpressionException):
            self.rpn.evaluate(Queue(deque(["5", "6", "!", "+"])))
