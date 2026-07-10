# 34. Implement a Queue for printer jobs

from collections import deque


class PrinterQueue:
    def __init__(self):
        self.jobs = deque()

    def enqueue_job(self, job_name):
        self.jobs.append(job_name)
        print(f"Added: {job_name}")

    def process_job(self):
        if self.jobs:
            job = self.jobs.popleft()
            print(f"Processing: {job}")
            return job
        print("No jobs in queue")
        return None


if __name__ == "__main__":
    printer = PrinterQueue()
    printer.enqueue_job("Report.pdf")
    printer.enqueue_job("Assignment.docx")
    printer.process_job()
    printer.process_job()
