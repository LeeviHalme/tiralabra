import unittest
from src.classes.shunting_yard import ShuntingYard, MalformedExpressionException

class TestAdvancedShuntingYard(unittest.TestCase):
    def setUp(self) -> None:
        self.shunting_yard = ShuntingYard()
    
    def test_empty_expression(self):
        with self.assertRaises(MalformedExpressionException):
            self.shunting_yard.parse("")

    def test_mismatched_parentheses(self):
        with self.assertRaises(MalformedExpressionException):
            self.shunting_yard.parse("5 + )6 * 2")

    # def test_division_by_zero(self):
    #     with self.assertRaises(MalformedExpressionException):
    #         self.shunting_yard.parse("5 / 0")
