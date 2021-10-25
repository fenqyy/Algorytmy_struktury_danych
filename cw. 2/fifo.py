from typing import Any


class LinkedList:

    def __init__(self, value):
        self.value: Any = value
        self.next: 'Node' = None


class Queue:

    def __init__(self):
        self.storage: LinkedList = None

    def peek(self) -> Any:
        tmp = self.storage
        while(tmp.next!=None):
            tmp = tmp.next
        return tmp.value

    def enqueue(self, element: Any) -> None:
        newNode = LinkedList(element)
        if self.storage == None:
            self.storage = newNode
        else:
            newNode.next = self.storage
            self.storage = newNode

    def dequeue(self) -> Any:
        tmp = self.storage
        while (tmp.next.next != None):
            tmp = tmp.next
        dequeueElement = tmp.next.value
        tmp.next = tmp.next.next
        return dequeueElement

    def __str__(self):
        li = []
        tmp = self.storage
        while (tmp != None):
            li.append(str(tmp.value))
            tmp = tmp.next
        return ', '.join(li[::-1])

    def __len__(self):
        iterator = 0
        tmp = self.storage
        while (tmp != None):
            iterator += 1
            tmp = tmp.next
        return iterator


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