from typing import Any
from linkedlist import LinkedList


class Stack:

    def __init__(self):
        self.storage = LinkedList()

    def push(self, element: Any) -> None:
        return self.storage.push(element)

    def pop(self) -> Any:
        return self.storage.pop()

    def __str__(self):
        return self.storage.__str__().replace(" -> ", "\n")

    def __len__(self):
        return self.storage.__len__()




stack = Stack()

assert len(stack) == 0

stack.push(3)
stack.push(10)
stack.push(1)



assert len(stack) == 3


top_value = stack.pop()

assert top_value == 1


assert len(stack) == 2
