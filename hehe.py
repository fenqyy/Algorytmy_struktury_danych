from typing import Any, Callable


class BinaryNode:

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def is_leaf(self):
        if not (self.left_child or self.right_child):
            return True
        return False

    def add_left_child(self, value: Any):
        tmp = BinaryNode(value)
        self.left_child = tmp

    def add_right_child(self, value: Any):
        tmp = BinaryNode(value)
        self.right_child = tmp

    def traverse_in_order(self, visit: Callable[[Any], None]):
        if(visit):
            traverse_in_order(self.left_child)
            print(visit.value)
            traverse_in_order(self.right_child)

    def __str__(self):
        return str(self.value)





class BinaryTree:

    def __init__(self, value=None):
        self.root = BinaryNode(value)
        self.value = value

    def __str__(self):
        return str(self.value)



tree = BinaryTree(10)

assert tree.root.value == 10

BinaryTree.add_left_child(1)






