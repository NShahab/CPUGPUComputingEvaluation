import json
import time
import matplotlib.pyplot as plt
import BarChartPlotterMultiMatrix
from performance_report.matrix_multiplier import MatrixMultiplier


def main():

    matrix_size = int(input("Enter the size of the matrix: "))

    matrix_multiplier = MatrixMultiplier(matrix_size)

    parallel_start_time = time.time()
    parallel_result = matrix_multiplier.multiply_parallel()
    parallel_end_time = time.time()

    serial_start_time = time.time()
    serial_result = matrix_multiplier.multiply_serial()
    serial_end_time = time.time()

    # Save the results to a JSON file
    results = {
        "Parallel multiplication result": round(parallel_result),
        "Serial multiplication result": round(serial_result),
        "Parallel multiplication time": round(parallel_end_time - parallel_start_time, 4),
        "Serial multiplication time": round(serial_end_time - serial_start_time, 4)
    }
    with open("res_matrix_multiplier.json", "w") as json_file:
        json.dump(results, json_file)


if __name__ == '__main__':
    main()
