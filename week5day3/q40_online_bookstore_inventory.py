# 40. Build a mini project that combines Binary Search, Merge Sort, Stack, and Queue to manage an online bookstore inventory

from collections import deque


class BookStore:
    def __init__(self, books):
        self.books = books
        self.cart_stack = []
        self.order_queue = deque()

    def merge_sort(self, items):
        if len(items) <= 1:
            return items
        mid = len(items) // 2
        left = self.merge_sort(items[:mid])
        right = self.merge_sort(items[mid:])
        return self._merge(left, right)

    def _merge(self, left, right):
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    def binary_search(self, target):
        sorted_books = self.merge_sort(self.books)
        low, high = 0, len(sorted_books) - 1
        while low <= high:
            mid = (low + high) // 2
            if sorted_books[mid] == target:
                return True
            if sorted_books[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False

    def add_to_cart(self, book):
        self.cart_stack.append(book)

    def checkout(self):
        while self.cart_stack:
            self.order_queue.append(self.cart_stack.pop())

    def process_order(self):
        if self.order_queue:
            return self.order_queue.popleft()
        return None


if __name__ == "__main__":
    bookstore = BookStore(["Python", "Java", "C++", "Go"])
    print("Sorted books:", bookstore.merge_sort(bookstore.books))
    print("Search for 'Java':", bookstore.binary_search("Java"))
    bookstore.add_to_cart("Python")
    bookstore.add_to_cart("Java")
    bookstore.checkout()
    print("Processed order:", bookstore.process_order())
