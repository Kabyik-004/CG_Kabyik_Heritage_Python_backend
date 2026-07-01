# 36. Implement BFS-ready queue operations using deque

from collections import deque


def bfs_queue_demo():
    queue = deque()
    queue.append("A")
    queue.append("B")
    queue.append("C")

    print("Queue before processing:", list(queue))
    while queue:
        node = queue.popleft()
        print("Visited:", node)


if __name__ == "__main__":
    bfs_queue_demo()
