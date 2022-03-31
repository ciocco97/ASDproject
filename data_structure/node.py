from data_structure.subset import Subset


class Node:
    def __init__(self, value: Subset, next_node=None, prev_node=None):
        self.value = value

        self.next = next_node
        self.prev = prev_node

    def get_value(self) -> Subset:
        return self.value

    def __str__(self):
        return str(self.value)

    def set_next(self, next_node):
        self.next = next_node

    def set_prev(self, prev_node):
        self.prev = prev_node

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev
