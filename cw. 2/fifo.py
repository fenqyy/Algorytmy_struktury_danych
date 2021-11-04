from typing import Any
from linkedlist import LinkedList


class Queue:

    def __init__(self):
        self.storage = LinkedList()

    def peek(self) -> Any:
        return self.storage

    def enqueue(self, element: Any) -> None:
        self.storage.append(element)

    def dequeue(self) -> Any:
        return self.storage.pop()

    def __str__(self):
        return self.storage.__str__().replace(" -> ", ", ")

    def __len__(self):
        return self.storage.__len__()


queue = Queue()

assert len(queue) == 0


queue.enqueue('klient1')
queue.enqueue('klient2')
queue.enqueue('klient3')



assert str(queue) == 'klient1, klient2, klient3'


client_first = queue.dequeue()




assert client_first == 'klient1'
assert str(queue) == 'klient2, klient3'
assert len(queue) == 2
