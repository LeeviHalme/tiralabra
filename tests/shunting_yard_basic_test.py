import unittest
from src.classes.shunting_yard import ShuntingYard
from src.classes.tokenizer import Tokenizer

class TestBasicShuntingYard(unittest.TestCase):
    def setUp(self) -> None:
        self.shunting_yard = ShuntingYard()
        self.t = Tokenizer()

    def test_verbose(self):
        self.shunting_yard = ShuntingYard(verbose=True)
        self.test_addition()

    def test_addition(self):
        result = self.shunting_yard.parse(self.t.tokenize("3 + 4")).to_list()
        self.assertEqual(result, ["3", "4", "+"])

    def test_subtraction(self):
        result = self.shunting_yard.parse(self.t.tokenize("10 - 2")).to_list()
        self.assertEqual(result, ["10", "2", "-"])

    def test_multiplication(self):
        result = self.shunting_yard.parse(self.t.tokenize("5 * 6")).to_list()
        self.assertEqual(result, ["5", "6", "*"])

    def test_big_addition(self):
        input_str = "1000 + 2000 - 3000 * 4000 / 5000"
        assertion = ["1000", "2000", "+", "3000", "4000", "*", "5000", "/", "-"]
        result = self.shunting_yard.parse(self.t.tokenize(input_str)).to_list()
        self.assertEqual(result, assertion)

    def test_operator_precedence(self):
        res = self.shunting_yard.parse(self.t.tokenize("3 + 4 * 2")).to_list()
        self.assertEqual(res, ["3", "4", "2", "*", "+"])

    def test_operator_precedence_parentheses(self):
        result = self.shunting_yard.parse(self.t.tokenize("(3 + 4) * 2")).to_list()
        self.assertEqual(result, ["3", "4", "+", "2", "*"])

    def test_negative(self):
        result = self.shunting_yard.parse(self.t.tokenize("(-5)")).to_list()
        self.assertEqual(result, ["-5"])

    def test_implicit_positive(self):
        result = self.shunting_yard.parse(self.t.tokenize("+2")).to_list()
        self.assertEqual(result, ["2"])

    def test_negative_multiplication(self):
        result = self.shunting_yard.parse(self.t.tokenize("3 * -4")).to_list()
        self.assertEqual(result, ["3", "*", "4", "-"])

    def test_constants(self):
        result = self.shunting_yard.parse(self.t.tokenize("pi")).to_list()
        self.assertEqual(result, ["pi"])

    def test_variables(self):
        result = self.shunting_yard.parse(self.t.tokenize("x")).to_list()
        self.assertEqual(result, ["x"])

    def test_sin(self):
        result = self.shunting_yard.parse(self.t.tokenize("sin(3)")).to_list()
        self.assertEqual(result, ["3", "sin"])

    def test_cos(self):
        result = self.shunting_yard.parse(self.t.tokenize("cos(3)")).to_list()
        self.assertEqual(result, ["3", "cos"])

    def test_min(self):
        result = self.shunting_yard.parse(self.t.tokenize("min(3, 4)")).to_list()
        self.assertEqual(result, ["3", "4", "min"])

    def test_max(self):
        result = self.shunting_yard.parse(self.t.tokenize("max(3, 4)")).to_list()
        self.assertEqual(result, ["3", "4", "max"])
