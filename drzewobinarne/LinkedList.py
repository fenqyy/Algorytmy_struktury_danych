from typing import Any


class Node:

    def __init__(self, value):
        self.value: Any = value
        self.next: 'Node' = None


class LinkedList:

    def __init__(self):
        self.head: Node = None

    def push(self, value: Any) -> None:
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def append(self,value: Any) -> None:
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
        else:
            tmp = self.head
            while tmp.next != None:
                tmp = tmp.next
            tmp.next = newNode

    def node(self, at: int) -> Node:
        iterator = 0
        tmp = self.head
        while(iterator != at):
            iterator+=1
            tmp = tmp.next
        return tmp

    def insert(self, value: Any, after: Node) -> None:
        newNode = Node(value)
        tmp = self.head
        while(tmp != after):
            tmp = tmp.next
        tmp2 = tmp.next
        tmp.next = newNode
        tmp.next.next = tmp2

    def pop(self) -> Any:
        returnedPop = self.head.value
        self.head = self.head.next
        return returnedPop

    def remove_last(self) -> Any:
        tmp = self.head
        while(tmp.next.next!=None):
            tmp = tmp.next
        lastElement = tmp.next.value
        tmp.next = tmp.next.next
        return lastElement

    def remove(self, after: Node) -> Any:
        tmp = self.head
        while(tmp != after):
            tmp = tmp.next
        tmp.next = tmp.next.next

    def __len__(self):
        iterator = 0
        tmp = self.head
        while(tmp != None):
            iterator+=1
            tmp = tmp.next
        return iterator

    def __str__(self):
        string = ""
        tmp = self.head
        while(tmp != None):
            string+=str(tmp.value)
            if tmp.next != None:
                string += " -> "
            tmp = tmp.next
        return string





list_ = LinkedList()

assert list_.head == None


list_.push(1)
list_.push(0)

assert str(list_) == '0 -> 1'

list_.append(9)
list_.append(10)

assert str(list_) == '0 -> 1 -> 9 -> 10'

middle_node = list_.node(at=1)
list_.insert(5, after=middle_node)

assert str(list_) == '0 -> 1 -> 5 -> 9 -> 10'


first_element = list_.node(at=0)
returned_first_element = list_.pop()

assert first_element.value == returned_first_element

last_element = list_.node(at=3)
returned_last_element = list_.remove_last()

assert last_element.value == returned_last_element

assert str(list_) == '1 -> 5 -> 9'


second_node = list_.node(at=1)

list_.remove(second_node)


assert str(list_) == '1 -> 5'