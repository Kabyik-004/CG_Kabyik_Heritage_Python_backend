# 39. Analyze the time complexity of push/pop on Python lists versus deque

from collections import deque
import time


def compare_performance(n=100000):
    lst = []
    dq = deque()

    start = time.time()
    for _ in range(n):
        lst.append(1)
    for _ in range(n):
        lst.pop()
    list_time = time.time() - start

    start = time.time()
    for _ in range(n):
        dq.append(1)
    for _ in range(n):
        dq.pop()
    deque_time = time.time() - start

    print("List time:", round(list_time, 6), "seconds")
    print("Deque time:", round(deque_time, 6), "seconds")


if __name__ == "__main__":
    compare_performance()
