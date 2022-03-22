from subset import Subset

class SubsQueue:
    def __init__(self):
        self.items = []
        self.items.insert(0, Subset([0]))

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
