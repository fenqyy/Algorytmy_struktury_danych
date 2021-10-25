from typing import Any


class LinkedList:

    def __init__(self, value):
        self.value: Any = value
        self.next: 'Node' = None


class Stack:

    def __init__(self):
        self.storage: LinkedList = None

    def push(self, element: Any) -> None:
        newNode = LinkedList(element)
        if self.storage == None:
            self.storage = newNode
        else:
            newNode.next = self.storage
            self.storage = newNode

    def pop(self) -> Any:
        popElement = self.storage.value
        self.storage = self.storage.next
        return popElement

    def __str__(self):
        li = []
        tmp = self.storage
        while (tmp != None):
            li.append(str(tmp.value))
            tmp = tmp.next
        return "\n".join(li[::-1])

    def __len__(self):
        iterator = 0
        tmp = self.storage
        while (tmp != None):
            iterator += 1
            tmp = tmp.next
        return iterator




stack = Stack()

assert len(stack) == 0

stack.push(3)
stack.push(10)
stack.push(1)



assert len(stack) == 3


top_value = stack.pop()

assert top_value == 1


assert len(stack) == 2