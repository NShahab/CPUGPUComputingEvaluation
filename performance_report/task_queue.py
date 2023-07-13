from queue import Queue


class TaskQueue:
    def __init__(self):
        self.queue = Queue()

    def add_task(self, task):
        self.queue.put(task)

    def get_task(self):
        return self.queue.get()

    def is_empty(self):
        return self.queue.empty()

    def task_count(self):
        return self.queue.qsize()
