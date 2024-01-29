from collections import deque

# Implementation of a queue using a deque
#
# Methods:
#   add(item: str) -> None: enqueues item onto queue
#   dequeue() -> str: dequeues item from queue
#   size() -> int: returns size of queue
class Queue:
    def __init__(self):
        self.queue = deque()

    def add(self, value: str) -> None:
        self.queue.append(value)

    def remove(self) -> str:
        if self.size() == 0:
            raise IndexError("remove from empty queue")
        return self.queue.popleft()

    def size(self) -> int:
        return len(self.queue)
    
    def __str__(self) -> str:
        return " ".join(self.queue)
