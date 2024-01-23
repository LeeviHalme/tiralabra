from collections import deque

# Implementation of a stack using a deque
#
# Methods:
#   is_empty() -> bool: returns boolean flag indicating if stack is empty
#   push(item: str) -> None: pushes item onto stack
#   pop() -> str: pops item from stack
#   peek() -> str: returns item at top of stack
#   size() -> int: returns size of stack
class Stack:
    def __init__(self) -> None:
        self.items = deque()

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def push(self, item: str) -> None:
        self.items.append(item)

    def pop(self) -> str:
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        return self.items.pop()

    def peek(self) -> str:
        if self.is_empty():
            raise IndexError("peek from an empty stack")
        return self.items[-1]

    def size(self) -> int:
        return len(self.items)
