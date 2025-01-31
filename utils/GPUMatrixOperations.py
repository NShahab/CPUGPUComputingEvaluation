import numpy as np
import cupy as cp
import time


# GPU Matrix Multiplication
def matrix_multiplication(matrix_size=1000): 
        matrix_a = np.random.rand(matrix_size, matrix_size)
        matrix_b = np.random.rand(matrix_size, matrix_size)
        start_time = time.time()

        # Perform matrix multiplication using GPU
        gpu_matrix_a = cp.asarray(matrix_a)
        gpu_matrix_b = cp.asarray(matrix_b)
        gpu_result = cp.dot(gpu_matrix_a, gpu_matrix_b)
        cpu_result = cp.asnumpy(gpu_result)

        end_time = time.time()
        execution_time = end_time - start_time
        return cpu_result, execution_time


