from .queue import Queue
from .stack import Stack
from .exceptions import MalformedExpressionException

class RPNEvaluator:
    def __init__(self, verbose: bool = False) -> None:
        self.verbose = verbose
        self.operators = set(["+", "-", "*", "/", "^"])
        self.stack = Stack()

    def __print(self, *args, **kwargs) -> None:
        if self.verbose:
            print(*args, **kwargs)

    def evaluate(self, tokens: Queue) -> int:
        tokens = tokens.copy()
        while tokens.size() > 0:
            token = tokens.remove()

            # push numbers straight to the stack
            if token.isdigit() or token.startswith("-") and len(token) > 1:
                self.__print(f"Pushing {token} to stack")
                self.stack.push(float(token))
                continue

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
                        self.__print(f"Ignoring unary plus, \
                                     pushing {num_2} back to stack")
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
                except IndexError as e:
                    raise MalformedExpressionException(
                        "Not enough operands for operator"
                    ) from e

            raise MalformedExpressionException(f"Invalid token: {token}")

        if self.stack.size() != 1:
            raise MalformedExpressionException("Too many operands for operator")

        return self.stack.pop()

    def __apply_operator(self, num_1: int, operator: str, num_2: int) -> int:
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
        except ZeroDivisionError as e:
            raise MalformedExpressionException("Division by zero") from e
