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
            self.rpn.evaluate(Queue(deque(["5", "0", "/"])), variables={})

    def too_few_operands(self):
        with self.assertRaises(MalformedExpressionException):
            self.rpn.evaluate(Queue(deque(["5", "*"])), variables={})

    def test_too_many_operands(self):
        with self.assertRaises(MalformedExpressionException):
            self.rpn.evaluate(Queue(deque(["5", "6", "+", "7"])), variables={})

    def test_invalid_operator(self):
        with self.assertRaises(MalformedExpressionException):
            self.rpn.evaluate(Queue(deque(["5", "6", "!", "+"])), variables={})

    def test_invalid_variable(self):
        with self.assertRaises(MalformedExpressionException):
            self.rpn.evaluate(Queue(deque(["5", "x", "+"])), variables={})

    def test_mismatched_parentheses_left(self):
        with self.assertRaises(MalformedExpressionException):
            self.rpn.evaluate(Queue(deque(["5", "+", "("])), variables={})

    def test_function_too_few_arguments(self):
        with self.assertRaises(MalformedExpressionException):
            self.rpn.evaluate(Queue(deque(["sin"])), variables={})
            self.rpn.evaluate(Queue(deque(["cos"])), variables={})
            self.rpn.evaluate(Queue(deque(["min"])), variables={})
            self.rpn.evaluate(Queue(deque(["1", "min"])), variables={})
            self.rpn.evaluate(Queue(deque(["max"])), variables={})
            self.rpn.evaluate(Queue(deque(["1", "max"])), variables={})

    def test_function_too_many_arguments(self):
        with self.assertRaises(MalformedExpressionException):
            self.rpn.evaluate(Queue(deque(["1", "2", "sin"])), variables={})
            self.rpn.evaluate(Queue(deque(["1", "2", "cos"])), variables={})
            self.rpn.evaluate(Queue(deque(["1", "2", "3", "min"])), variables={})
            self.rpn.evaluate(Queue(deque(["1", "2", "3", "max"])), variables={})
