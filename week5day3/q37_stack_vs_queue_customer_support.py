# 37. Compare Stack and Queue using a customer-support example


class SupportSystem:
    def __init__(self):
        self.stack = []
        self.queue = []

    def add_issue(self, issue):
        self.stack.append(issue)
        self.queue.append(issue)

    def resolve_latest_issue(self):
        if self.stack:
            return self.stack.pop()
        return None

    def resolve_earliest_issue(self):
        if self.queue:
            return self.queue.pop(0)
        return None


if __name__ == "__main__":
    support = SupportSystem()
    support.add_issue("Login error")
    support.add_issue("Payment issue")
    print("Latest issue resolved:", support.resolve_latest_issue())
    print("Earliest issue resolved:", support.resolve_earliest_issue())
