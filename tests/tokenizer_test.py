import unittest
from src.classes.tokenizer import Tokenizer

class TestTokenizer(unittest.TestCase):
    def setUp(self) -> None:
        self.tokenizer = Tokenizer()

    def test_simple_expression(self):
        exp =  "3 + 4 * 2 / ( 1 - 5 ) ^ 2"
        expected = ["3", "+", "4", "*", "2", "/", \
                     "(", "1", "-", "5", ")", "^", "2"]
        self.assertEqual(self.tokenizer.tokenize(exp), expected)

    def test_expression_with_spaces(self):
        exp =  "   3   +   4   *   2   /   (   1   -   5   )   ^   2   "
        expected = ["3", "+", "4", "*", "2", "/", "(", \
                     "1", "-", "5", ")", "^", "2"]
        self.assertEqual(self.tokenizer.tokenize(exp), expected)

    def test_expression_with_exponents(self):
        exp =  "2^3 + 4^(5-2)"
        expected =  ["2", "^", "3", "+", "4", "^", "(", "5", "-", "2", ")"]
        self.assertEqual(self.tokenizer.tokenize(exp), expected)

    def test_expression_with_negatives(self):
        exp =  "-3 + (-4) * -2"
        expected = ["-3", "+", "(", "-4", ")", "*", "-", "2"]
        self.assertEqual(self.tokenizer.tokenize(exp), expected)

    # def test_expression_with_variables(self):
    #     exp =  "x + y * ( z - 5 ) ^ 2"
    #     expected = ["x", "+", "y", "*", "(", "z", "-", "5", ")", "^", "2"]
    #     self.assertEqual(self.tokenizer.tokenize(exp), expected)

    # def test_expression_with_functions(self):
    #     exp =  "sin(x) + cos(y) * tan(z)"
    #     expected = ["sin", "(", "x", ")", "+", "cos", "(", "y", ")", "*", "tan", "(", "z", ")"]
    #     self.assertEqual(self.tokenizer.tokenize(exp), expected)

    # def test_expression_with_extra_operators(self):
    #     exp =  "2*3 + 4//2 - 5%2"
    #     expected = ["2", "*", "3", "+", "4", "//", "2", "-", "5", "%", "2"]
    #     self.assertEqual(self.tokenizer.tokenize(exp), expected)