from .stack import Stack
from .queue import Queue
from .exceptions import MalformedExpressionException

# Implementation of the shunting yard algorithm
#
# Methods:
# - print: prints out the algorithm steps if verbose mode is enabled
# - parse_right_parenthesis:
#     pops operators off the stack until a left parenthesis is found
# - has_higher_precedence: checks if op1 has higher precedence than op2
# - parse: parses the expression (list of tokens) and returns the output queue
class ShuntingYard:
    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.op_stack = Stack()
        self.output_queue = Queue()
        self.operators = set(["+", "-", "*", "/", "^"])
        self.precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}

    def __print(self, *args, **kwargs) -> None:
        if self.verbose:
            print(*args, **kwargs)

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
            raise MalformedExpressionException("Mismatched parenthesis! (different number of left and right parenthesis)")

    def has_higher_precedence(self, op1: str, op2: str) -> bool:
        # check if op1 has higher precedence than op2
        # (only power op is right-associative)
        return self.precedence.get(op1, 0) > self.precedence.get(op2, 0) or \
          (self.precedence.get(op1, 0) == self.precedence.get(op2, 0) \
          and op1 != "^")

    # pylint: disable=too-many-statements
    def parse(self, expression: list) -> Queue:
        # if expression is empty, raise an exception
        if len(expression) == 0:
            raise MalformedExpressionException("Empty expression!")

        # iterate through the expression
        # pylint: disable=too-many-nested-blocks
        for token in expression:
            # if token is a number (positive or negative)
            if token.isdigit() or token.startswith("-") and len(token) > 1:
                self.__print("Add token to output", token)

                # add the number to the output queue
                self.output_queue.add(token)
                continue

            # pylint: disable=fixme
            # TODO: parse functions and constants

            # if token is an operator
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

        self.__print("Pop entire stack to output")

        # pop all operators off the stack and add them to the output queue
        while self.op_stack.size() > 0:
            self.output_queue.add(self.op_stack.pop())

        return self.output_queue
