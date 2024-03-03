import unittest
from src.classes.token_list import TokenList

class TestTokenList(unittest.TestCase):
    def test_is_variable_assignment(self) -> None:
        var_list = TokenList([], {"a": TokenList(["1"], {})})
        no_var_list = TokenList(["1", "+", "2"], {})
        self.assertTrue(var_list.is_variable_assignment())
        self.assertFalse(no_var_list.is_variable_assignment())

    def test_str(self) -> None:
        var_list = TokenList(["1", "+", "2"], {"a": TokenList(["1"], {})})
        self.assertEqual(
            str(var_list),
            "\n Tokens: [1, +, 2] \n Variables: a: ['1']",
        )
