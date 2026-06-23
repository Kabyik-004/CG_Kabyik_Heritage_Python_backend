# Create a fresh stack
class Stack:
    def __init__(self):
        self._items = []

    def push(self, v): self._items.append(v)
    def pop(self): return self._items.pop() if self._items else None
    def is_empty(self): return len(self._items) == 0
    def size(self): return len(self._items)
    def __repr__(self): return repr(self._items)


book_stack = Stack()
 
# Push books one at a time (simulating placing on a desk)
book_stack.push("Python Basics")       # First book — goes to bottom
book_stack.push("Data Structures")
book_stack.push("Algorithms")
book_stack.push("System Design")
book_stack.push("Clean Code")          # Last book — sits on TOP
 
print(book_stack)                       # Show state
print(f'Total books stacked: {book_stack.size()}')
print(f'Top book right now: {book_stack.peek()}')
