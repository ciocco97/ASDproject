class SubsQueue:
    def __init__(self):
        self.items = []
        self.items.insert(0, 0)

    def enqueue(self, item):
        self.items.insert(len(self.items), item)

    def dequeue(self):
        return self.items.pop()
