from subset import Subset

class SubsQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(len(self.items), item)

    def dequeue(self):
        return self.items.pop()