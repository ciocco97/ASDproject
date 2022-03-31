from data_structure.subset import Subset
from data_structure.node import Node


class SubsQueue:
    def __init__(self):
        self.size = 1
        self.head = self.tail = Node(Subset([0]))

    def enqueue(self, item: Subset):
        self.size += 1

        if self.size == 1:
            self.head = self.tail = Node(item)
        else:
            new_node = Node(item, None, self.tail)
            self.tail.set_next(new_node)
            self.tail = new_node

    def dequeue(self) -> Subset:
        self.size -= 1

        sub = self.head.get_value()

        if self.size > 0:
            self.head = self.head.get_next()
            self.head.set_prev(None)

        return sub

    def get_size(self) -> int:
        return self.size
