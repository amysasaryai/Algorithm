class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.insert(len(self.items),item)

    def dequeue(self):
        return self.items.pop(0)

q = Queue()
print q.isEmpty
print q.items
print q.size
print q.enqueue(5)
print q.enqueue(6)
print q.enqueue(9)
print q.dequeue()
print q.size
print q.items


