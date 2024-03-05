import string
from .exceptions import MalformedExpressionException
from .token_list import TokenList

# This class is responsible for tokenizing the input expression
# into a list of tokens to be used by the Shunting Yard algorithm.
#
# Methods:
# - tokenize: returns a TokenList from the input expression
# - is_variable_assignment: returns True if the expression is a variable assignment
# pylint: disable=too-few-public-methods
class Tokenizer:
    def __init__(self):
        # changing these will affect the rpn evaluator
        self.operators = set(["+", "-", "*", "/", "^", "(", ")", "="])
        self.functions = set(["sin", "cos", "tan", "sqrt", "min", "max"])
        self.constants = set(["pi"])
        self.variables = set(string.ascii_lowercase)

    def is_variable_assignment(self, expression: str) -> bool:
        return "=" in expression

    def assign_variable(self, tokens: list) -> TokenList:
        # check the syntax
        if (len(tokens) < 3 or tokens[0] not in self.variables or tokens[1] != "="):
            raise MalformedExpressionException(
                "Invalid variable assignment syntax. Example usage: x = 2"
            )

        return TokenList([], { tokens[0]: TokenList(tokens[2:], {}) })

    # pylint: disable=too-many-statements
    def tokenize(self, expression: str) -> TokenList:
        tokens = []
        negative = False
        num_start = None  # to keep track of the start index of a number

        if len(expression) == 0:
            raise MalformedExpressionException("Empty expression!")

        # pylint: disable=too-many-nested-blocks
        skip_until_index = 0
        for i, char in enumerate(expression):
            # skip characters that have already been processed
            if i < skip_until_index:
                continue

            # check if previous and next index can be accessed
            is_in_middle = 0 < i < (len(expression) - 1)

            # if current character is a digit
            if char.isdigit():
                if num_start is None:
                     # set the start index of the number
                    num_start = i
                    continue
                continue

            if num_start is not None:
                # number ends if it has started
                number = expression[num_start:i].strip()
                tokens.append(f"-{number}" if negative else number)
                negative = False
                num_start = None

            # handle one parameter functions
            if expression[i:i + 3] in self.functions:
                tokens.append(expression[i:i + 3])
                skip_until_index = i + 3
                continue

            # handle two parameter functions
            if expression[i:i + 4] in self.functions:
                tokens.append(expression[i:i + 4])
                skip_until_index = i + 4
                continue

            # handle constants
            if expression[i:i + 2] in self.constants:
                tokens.append(expression[i:i + 2])
                skip_until_index = i + 2
                continue

            # handle variables
            if char in self.variables:
                tokens.append(char)
                continue

            # handle operators
            if char in self.operators:
                first_match = i == 0 and len(expression) > 1 and expression[i + 1].isdigit()

                # if current character is a negative sign
                if char == "-":
                    # if the negative sign is a unary negation (previous char is
                    # a space (or left parenthesis) and next char is a digit
                    # OR first to match)
                    if first_match or (is_in_middle and \
                      (expression[i - 1] == "" or expression[i - 1] == "(") \
                      and expression[i + 1].isdigit()):
                        negative = True
                        continue

                # if current character is a plus sign
                elif char == "+":
                    # if the plus sign is used to implicitly denote a positive
                    # number (previous char is a space (or left parenthesis) and
                    # next char is a digit)
                    if first_match or (is_in_middle and \
                      (expression[i - 1] == "" or expression[i - 1] == "(") \
                      and expression[i + 1].isdigit()):
                        negative = False
                        continue

                # otherwise, add the operator to tokens
                tokens.append(char)
                continue

            # ignore spaces and commas
            if char.isspace() or char == ",":
                continue

            # token was not processed
            raise MalformedExpressionException("Invalid character" \
                                               f" '{char}' at position {i + 1}")

        # if the expression ends with a number, add it to tokens
        if num_start is not None:
            tokens.append(expression[num_start:].strip())

        # handle variable assignments
        if self.is_variable_assignment(expression):
            return self.assign_variable(tokens)

        return TokenList(tokens, {})
