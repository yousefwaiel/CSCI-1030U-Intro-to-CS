class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return f"[ {' '.join(map(str, self.items))} ]"