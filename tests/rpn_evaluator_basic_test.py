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
        result = self.rpn.evaluate(Queue(deque(["3", "4", "+"])))
        self.assertEqual(result, 7)

    def test_subtraction(self):
        result = self.rpn.evaluate(Queue(deque(["10", "2", "-"])))
        self.assertEqual(result, 8)

    def test_multiplication(self):
        result = self.rpn.evaluate(Queue(deque(["5", "6", "*"])))
        self.assertEqual(result, 30)

    def test_division(self):
        result = self.rpn.evaluate(Queue(deque(["10", "2", "/"])))
        self.assertEqual(result, 5)

    def test_power(self):
        result = self.rpn.evaluate(Queue(deque(["2", "2", "2", "^", "^"])))
        self.assertEqual(result, 16)

    def test_unary_negation(self):
        result = self.rpn.evaluate(Queue(deque(["-1", "-"])))
        self.assertEqual(result, 1)
    
    def test_unary_plus(self):
        result = self.rpn.evaluate(Queue(deque(["1", "+"])))
        self.assertEqual(result, 1)
