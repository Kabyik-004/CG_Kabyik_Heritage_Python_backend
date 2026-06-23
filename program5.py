# Simulate a busy bank branch with a queue


class Queue:
    def __init__(self):
        self._items = []

    def enqueue(self, v):
        self._items.append(v)

    def dequeue(self):
        return self._items.pop(0) if self._items else None

    def peek(self):
        return self._items[0] if self._items else None

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

    def __repr__(self):
        return repr(self._items)

branch = Queue()
 
# Customers arrive throughout the morning
print('--- Customers arriving ---')
branch.enqueue({"name": "Priya",   "service": "Loan inquiry"})
branch.enqueue({"name": "Rajan",   "service": "Cash withdrawal"})
branch.enqueue({"name": "Sunita",  "service": "Account opening"})
branch.enqueue({"name": "Akash",   "service": "FD renewal"})
 
print(f'Customers waiting: {branch.size()}')
next_cust = branch.peek()
print(f'Next to be served: {next_cust["name"]} ({next_cust["service"]})')
 
# Teller opens and serves customers (FIFO)
print()
print('--- Teller serving customers ---')
while not branch.is_empty():
    customer = branch.dequeue()
    print(f'  Serving: {customer["name"]:<10} | Service: {customer["service"]}')
    print(f'  Remaining in queue: {branch.size()}')
 
print()
print('All customers served!')
