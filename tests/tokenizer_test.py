import unittest
from src.classes.tokenizer import Tokenizer
from src.classes.exceptions import MalformedExpressionException

class TestTokenizer(unittest.TestCase):
    def setUp(self) -> None:
        self.tokenizer = Tokenizer()

    def test_simple_expression(self):
        exp =  "3 + 4 * 2 / ( 1 - 5 ) ^ 2"
        expected = ["3", "+", "4", "*", "2", "/", \
                     "(", "1", "-", "5", ")", "^", "2"]
        result = self.tokenizer.tokenize(exp)
        self.assertEqual(result.tokens, expected)

    def test_expression_with_spaces(self):
        exp =  "   3   +   4   *   2   /   (   1   -   5   )   ^   2   "
        expected = ["3", "+", "4", "*", "2", "/", "(", \
                     "1", "-", "5", ")", "^", "2"]
        result = self.tokenizer.tokenize(exp)
        self.assertEqual(result.tokens, expected)

    def test_expression_with_exponents(self):
        exp =  "2^3 + 4^(5-2)"
        expected =  ["2", "^", "3", "+", "4", "^", "(", "5", "-", "2", ")"]
        result = self.tokenizer.tokenize(exp)
        self.assertEqual(result.tokens, expected)

    def test_expression_with_negatives(self):
        exp =  "-3 + (-4) * -2"
        expected = ["-3", "+", "(", "-4", ")", "*", "-", "2"]
        result = self.tokenizer.tokenize(exp)
        self.assertEqual(result.tokens, expected)

    def test_invalid_character(self):
        with self.assertRaises(MalformedExpressionException):
            self.tokenizer.tokenize("3 + 4 * 2 ^ 2 $")

    def test_variable_assignment(self):
        exp = "x = 5 * 5"
        result = self.tokenizer.tokenize(exp)
        self.assertEqual(result.tokens, ["x", "=", "5", "*", "5"])
        self.assertEqual(result.variables.get("x").tokens, ["5", "*", "5"])

    def test_invalid_assignment(self):
        with self.assertRaises(MalformedExpressionException):
            self.tokenizer.tokenize("=")
            self.tokenizer.tokenize("= 5 * 5 +")
            self.tokenizer.tokenize("x = 5 * 5 +")
            self.tokenizer.tokenize("x = 5 * 5 + y")
            self.tokenizer.tokenize("ö = 5 * 5")
            self.tokenizer.tokenize("x = 5 * 5 = 6")
