from string import ascii_lowercase
from .stack import Stack
from .queue import Queue
from .exceptions import MalformedExpressionException
from .token_list import TokenList

# Implementation of the shunting yard algorithm
#
# Methods:
# - __print: prints out the algorithm steps if verbose mode is enabled
# - parse_right_parenthesis:
#     pops operators off the stack until a left parenthesis is found
# - has_higher_precedence: checks if op1 has higher precedence than op2
# - parse: parses the expression (list of tokens) and returns the output queue
class ShuntingYard:
    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.op_stack = Stack()
        self.output_queue = Queue()
        self.constants = set(["pi"])
        self.functions = set(["sin", "cos", "max", "min"])
        self.operators = set(["+", "-", "*", "/", "^"]) | self.functions
        self.precedence = {"+": 1, "-": 1, "*": 2, "/": 2, \
                          "^": 3, "cos": 4, "sin": 4, "max": 1, "min": 1}
        self.variables = set(ascii_lowercase)

    def __print(self, *args, **kwargs) -> None:
        if self.verbose:
            print("ShuntingYard:", *args, **kwargs)

    def parse_right_parenthesis(self) -> None:
        parenthesis_mismatch = True

        # pop operators off the stack until a left parenthesis is found
        while self.op_stack.size() > 0:
            # left parenthesis is found
            if self.op_stack.peek() == "(":
                parenthesis_mismatch = False
                self.__print("Pop stack", self.op_stack.peek())
                # pop the left parenthesis off the stack and discard it
                self.op_stack.pop()
                break

            self.__print("Pop stack to output", self.op_stack.peek())
            # add the operator to the output queue
            self.output_queue.add(self.op_stack.pop())

        # if no left parenthesis was found, the expression is malformed
        if parenthesis_mismatch:
            # pylint: disable=line-too-long
            raise MalformedExpressionException("Unmatched parenthesis! (missing left parenthesis)")

    def has_higher_precedence(self, op1: str, op2: str) -> bool:
        # check if op1 has higher precedence than op2
        # (only power op is right-associative)
        return self.precedence.get(op1, 0) > self.precedence.get(op2, 0) or \
          (self.precedence.get(op1, 0) == self.precedence.get(op2, 0) \
          and op1 != "^")

    # pylint: disable=too-many-statements
    def parse(self, expression: TokenList) -> Queue:
        # reset class variables
        self.op_stack = Stack()
        self.output_queue = Queue()

        # iterate through the expression
        # pylint: disable=too-many-nested-blocks
        for token in expression.tokens:
            # if token is a number (positive or negative)
            if token.isdigit() or token.startswith("-") and len(token) > 1:
                self.__print("Add token to output", token)

                # add the number to the output queue
                self.output_queue.add(token)
                continue

            # handle variables and constants
            if token in self.variables or token in self.constants:
                self.__print("Add token to output", token)

                # add the variable to the output queue
                self.output_queue.add(token)
                continue

            # if token is an operator or function
            if token in self.operators:
                # check for precedence: while (there is an operator o2 at the
                # top of the operator stack which is not a left parenthesis,
                # and (o2 has greater precedence than o1 or (o1 and o2 have
                # the same precedence and o1 is left-associative)
                while self.op_stack.size() > 0 and self.op_stack.peek() != "(" \
                and self.has_higher_precedence(self.op_stack.peek(), token):
                    self.__print("Pop stack to output", token)

                    # add the operator to the output queue
                    self.output_queue.add(self.op_stack.pop())

                self.__print("Push token to stack", token)

                # add the operator to the output queue
                self.op_stack.push(token)
                continue

            # if token is a left parenthesis
            if token == "(":
                self.__print("Push token to stack", token)

                # push the left parenthesis onto the stack
                self.op_stack.push(token)
                continue

            # if token is a right parenthesis
            if token == ")":
                self.parse_right_parenthesis()
                continue

            raise MalformedExpressionException(f"{token} is not implemented yet!")

        self.__print("Pop entire stack to output")

        # pop all operators off the stack and add them to the output queue
        while self.op_stack.size() > 0:
            self.output_queue.add(self.op_stack.pop())

        return self.output_queue
