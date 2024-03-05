from math import sin, cos, radians, pi
from string import ascii_lowercase
from .queue import Queue
from .stack import Stack
from .exceptions import MalformedExpressionException

# Implementation of the RPN evaluator algorithm
#
# Methods:
# - __print: prints out the algorithm steps if verbose mode is enabled
# - evaluate: evaluates the expression using the RPN algorithm
# - __apply_operator: applies the operator to the two operands
class RPNEvaluator: # pylint: disable=too-few-public-methods
    def __init__(self, verbose: bool = False) -> None:
        self.verbose = verbose
        self.stack = Stack()

        # changing these will affect the tokenizer
        self.operators = set(
            ["+", "-", "*", "/", "^"]
        )
        self.two_arg_functions = set(["min", "max"])
        self.functions = set(["sin", "cos"]) | self.two_arg_functions
        self.constants = set(["pi"])
        self.variables = set(ascii_lowercase) | self.constants

    def __print(self, *args, **kwargs) -> None:
        if self.verbose:
            print("RNPEvaluator:", *args, **kwargs)

    def evaluate(self, tokens: Queue, variables: dict) -> int: # pylint: disable=too-many-statements
        tokens = tokens.copy()
        self.__print("Evaluating", tokens, "with variables", variables)
        while tokens.size() > 0:
            token = tokens.remove()

            # push numbers straight to the stack
            if token.isdigit() or token.startswith("-") and len(token) > 1:
                self.__print(f"Pushing {token} to stack")
                self.stack.push(float(token))
                continue

            # handle constants
            if token in self.constants:
                self.__print(f"Constant: {token}")
                match token:
                    case "pi":
                        self.__print("Pushing π to stack", pi)
                        self.stack.push(pi)
                        continue

            # handle variables
            if token in self.variables:
                self.__print(f"Variable: {token}")
                try:
                    self.__print(f"Pushing {variables[token]} to stack")
                    self.stack.push(float(variables[token]))
                    continue
                except KeyError as error:
                    raise MalformedExpressionException(
                        f"Variable {token} is not assigned and has no value"
                    ) from error

            # handle operators
            if token in self.operators:
                self.__print(f"Operator: {token}")
                try:
                    num_2 = self.stack.pop()
                    self.__print(f"Popped {num_2} from stack")

                    # if this is unary negation, push it to the stack
                    if token == "-" and self.stack.size() == 0:
                        res = -float(num_2)
                        self.__print(f"Unary negation, pushing {res} to stack")
                        self.stack.push(res)
                        continue

                    # if this is unary plus, ignore it
                    if token == "+" and self.stack.size() == 0:
                        self.__print("Ignoring unary plus, " \
                                    f"pushing {num_2} back to stack")
                        self.stack.push(num_2)
                        continue

                    num_1 = self.stack.pop()
                    self.__print(f"Popped {num_1} from stack")

                    self.__print(f"Applying operation {num_1} {token} {num_2}")
                    res = self.__apply_operator(float(num_1), \
                                                token, float(num_2))

                    self.__print(f"Pushing {res} to stack")
                    self.stack.push(res)
                    continue
                except IndexError as error:
                    raise MalformedExpressionException(
                        "Not enough operands for operator"
                    ) from error

            # handle functions
            if token in self.functions:
                self.__print(f"Function: {token}")
                try:
                    num_2 = self.stack.pop()
                    self.__print(f"Popped {num_2} from stack")

                    # handle two argument functions
                    if token in self.two_arg_functions:
                        num_1 = self.stack.pop()
                        self.__print(f"Popped {num_1} from stack")

                        self.__print(f"Applying function {token}({num_1}, {num_2})")
                        res = self.__apply_operator(float(num_1), token, float(num_2))

                        self.__print(f"Pushing {res} to stack")
                        self.stack.push(res)
                        continue

                    self.__print(f"Applying function {token}({num_2})")
                    res = self.__apply_operator(0, token, float(num_2))

                    self.__print(f"Pushing {res} to stack")
                    self.stack.push(res)
                    continue
                except IndexError as error:
                    raise MalformedExpressionException(
                        "Not enough operands for function"
                    ) from error

            if token == "(":
                raise MalformedExpressionException(
                    "Unmatched parenthesis! (missing right parenthesis)"
                )
            raise MalformedExpressionException(f"Invalid token: {token}")

        if self.stack.size() != 1:
            raise MalformedExpressionException("Too many operands for operator")

        return self.stack.pop()

    def __apply_operator(self, num_1: int, operator: str, num_2: int) -> int: # pylint: disable=too-many-return-statements
        try:
            match operator:
                case "+":
                    return num_1 + num_2
                case "-":
                    return num_1 - num_2
                case "*":
                    return num_1 * num_2
                case "/":
                    return num_1 / num_2
                case "^":
                    return num_1 ** num_2
                case "sin":
                    return sin(radians(num_2))
                case "cos":
                    return cos(radians(num_2))
                case "min":
                    return min(num_1, num_2)
                case "max":
                    return max(num_1, num_2)
        except ZeroDivisionError as error:
            raise MalformedExpressionException("Division by zero") from error
        except OverflowError as error:
            raise MalformedExpressionException(
                "Result exceeded Python's runtime value limit. Try smaller calculations"
            ) from error
