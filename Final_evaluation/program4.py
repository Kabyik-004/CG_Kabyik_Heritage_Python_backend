# Q4 Part A: Balanced Parentheses

from collections import deque


def is_balanced(expr):
    stack = []

    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for ch in expr:

        if ch in "([{":
            stack.append(ch)

        elif ch in ")]}":

            if not stack:
                return False

            if stack.pop() != pairs[ch]:
                return False

    return len(stack) == 0


tests = [
    "()",
    "()[]{}",
    "(]",
    "([{}])",
    "((("
]

print("Balanced Parentheses\n")

for t in tests:
    print(t, "->", is_balanced(t))


# Part B Queue

queue = deque()

print("\nQueue Simulation")

queue.append("Alice")
print(queue)

queue.append("Bob")
print(queue)

queue.append("Charlie")
print(queue)

served = queue.popleft()
print("Served:", served)
print(queue)

served = queue.popleft()
print("Served:", served)
print(queue)
"""Balanced Parentheses

() -> True
()[]{} -> True
(] -> False
([{}]) -> True
((( -> False

Queue Simulation
deque(['Alice'])
deque(['Alice', 'Bob'])
deque(['Alice', 'Bob', 'Charlie'])
Served: Alice
deque(['Bob', 'Charlie'])
Served: Bob
deque(['Charlie'])"""