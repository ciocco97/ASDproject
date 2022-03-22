from subset import Subset

class SubsQueue:
    def __init__(self):
        self.items = []
        self.items.insert(0, Subset(0))

    def enqueue(self, item):
        self.items.insert(len(self.items), item)

    def dequeue(self):
        return self.items.pop()

    def mamma(self):
        return len(self.items)
