# 35. Simulate ticket booking requests using collections.deque

from collections import deque


class TicketBookingSystem:
    def __init__(self):
        self.requests = deque()

    def add_request(self, name):
        self.requests.append(name)
        print(f"Request added: {name}")

    def process_request(self):
        if self.requests:
            name = self.requests.popleft()
            print(f"Processing request for: {name}")
            return name
        print("No pending requests")
        return None


if __name__ == "__main__":
    booking = TicketBookingSystem()
    booking.add_request("Alice")
    booking.add_request("Bob")
    booking.process_request()
    booking.process_request()
