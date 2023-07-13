import random
import threading
import queue
import multiprocessing


class MatrixMultiplier:
    def __init__(self, matrix_size):
        self.matrix_size = matrix_size
        self.matrix = [[random.randint(1, 10) for _ in range(
            matrix_size)] for _ in range(matrix_size)]
        self.results = []
        self.total_sum = 0
        self.task_queue = queue.Queue()

    def calculate_row(self, row):
        try:
            result = sum(row)
            return result
        except Exception as e:
            print(f"Error in calculation: {str(e)}")

    def worker(self):
        while True:
            row = self.task_queue.get()
            if row is None:
                break
            result = self.calculate_row(row)
            self.results.append(result)
            self.total_sum += result  # Add the result to the total sum
            self.task_queue.task_done()

    def multiply_serial(self):
        matrix_size = len(self.matrix)
        result = [[0 for _ in range(matrix_size)] for _ in range(matrix_size)]

        for i in range(matrix_size):
            for j in range(matrix_size):
                for k in range(matrix_size):
                    result[i][j] += self.matrix[i][k] * self.matrix[k][j]

        return sum(sum(row) for row in result)

    def multiply_parallel(self):
        num_threads = min(self.matrix_size, multiprocessing.cpu_count())
        threads = []

        for _ in range(num_threads):
            thread = threading.Thread(target=self.worker)
            thread.start()
            threads.append(thread)

        for row in self.matrix:
            self.task_queue.put(row)

        self.task_queue.join()
        for _ in range(num_threads):
            self.task_queue.put(None)
        for thread in threads:
            thread.join()

        return self.total_sum  # Return the total sum
