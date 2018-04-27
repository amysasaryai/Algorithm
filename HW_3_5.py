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
q.enqueue(6)
q.enqueue(5)
q.enqueue(9)
q.dequeue()

print q.isEmpty()
print q.items
print q.size()






