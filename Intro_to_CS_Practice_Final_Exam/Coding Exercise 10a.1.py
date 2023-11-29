class Stack:
    def __init__(self):
        self._elements = []

    def top(self):
        return self._elements[0]

    def pop(self):
        top_element = self._elements[0]
        self._elements.pop(0)
        return top_element

    def push(self, new_element):
        self._elements.insert(0, new_element)

    def is_empty(self):
        return len(self._elements) == 0

    def print(self):
        for elem in self._elements:
            print(elem)


stack2 = Stack()
stack2.push('A')
stack2.push('B')
stack2.push('C')
print(f'{stack2.pop() = }')
print(f'{stack2.pop() = }')
print(f'{stack2.pop() = }')