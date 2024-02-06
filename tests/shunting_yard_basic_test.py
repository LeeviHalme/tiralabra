import unittest
from src.classes.shunting_yard import ShuntingYard, MalformedExpressionException

class TestBasicShuntingYard(unittest.TestCase):
    def setUp(self) -> None:
        self.shunting_yard = ShuntingYard()

    def test_output_basic(self):
        self.assertEqual(
            self.shunting_yard.parse("3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3"), \
                "3 4 2 * 1 5 - 2 3 ^ ^ / +")

    # test invalid parentehsis count
    def test_invalid_parenthesis(self):
        with self.assertRaises(MalformedExpressionException):
            self.shunting_yard.parse("3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3 )")