import unittest
from src.classes.tokenizer import Tokenizer
from src.classes.shunting_yard import ShuntingYard
from src.classes.exceptions import MalformedExpressionException

class TestAdvancedShuntingYard(unittest.TestCase):
    def setUp(self) -> None:
        self.shunting_yard = ShuntingYard()
        self.t = Tokenizer()

    def test_empty_expression(self):
        with self.assertRaises(MalformedExpressionException):
            self.shunting_yard.parse(self.t.tokenize(""))

    def test_mismatched_parentheses(self):
        with self.assertRaises(MalformedExpressionException):
            self.shunting_yard.parse(self.t.tokenize("5 + )6 * 2"))
