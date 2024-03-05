import math
import unittest
from collections import deque
from src.classes.queue import Queue
from src.classes.rpn_evaluator import RPNEvaluator

class TestBasicRPNEvaluator(unittest.TestCase):
    def setUp(self) -> None:
        self.rpn = RPNEvaluator()

    def test_verbose(self):
        self.rpn = RPNEvaluator(verbose=True)
        self.test_addition()

    def test_addition(self):
        result = self.rpn.evaluate(Queue(deque(["3", "4", "+"])), variables={})
        self.assertEqual(result, 7)

    def test_subtraction(self):
        result = self.rpn.evaluate(Queue(deque(["10", "2", "-"])), variables={})
        self.assertEqual(result, 8)

    def test_multiplication(self):
        result = self.rpn.evaluate(Queue(deque(["5", "6", "*"])), variables={})
        self.assertEqual(result, 30)

    def test_division(self):
        result = self.rpn.evaluate(Queue(deque(["10", "2", "/"])), variables={})
        self.assertEqual(result, 5)

    def test_power(self):
        result = self.rpn.evaluate(Queue(deque(["2", "2", "2", "^", "^"])), variables={})
        self.assertEqual(result, 16)

    def test_unary_negation(self):
        result = self.rpn.evaluate(Queue(deque(["-1", "-"])), variables={})
        self.assertEqual(result, 1)

    def test_unary_plus(self):
        result = self.rpn.evaluate(Queue(deque(["1", "+"])), variables={})
        self.assertEqual(result, 1)

    def test_constants(self):
        result = self.rpn.evaluate(Queue(deque(["pi"])), variables={})
        self.assertEqual(result, math.pi)

    def test_variables(self):
        result = self.rpn.evaluate(Queue(deque(["1", "x", "+"])), variables={"x": 5})
        self.assertEqual(result, 6)

    def test_sin(self):
        result = self.rpn.evaluate(Queue(deque(["0", "sin"])), variables={})
        self.assertEqual(result, 0)

    def test_cos(self):
        result = self.rpn.evaluate(Queue(deque(["0", "cos"])), variables={})
        self.assertEqual(result, 1)

    def test_max(self):
        result = self.rpn.evaluate(Queue(deque(["5", "6", "max"])), variables={})
        self.assertEqual(result, 6)

    def test_min(self):
        result = self.rpn.evaluate(Queue(deque(["5", "6", "min"])), variables={})
        self.assertEqual(result, 5)
