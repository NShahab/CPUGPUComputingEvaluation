import json
import time
from utils.cpu_operations import cpu_operations
import PlotLineChart
import matplotlib.pyplot as plt
import plot_average_from_json
import BarChartPlotterMultiMatrix
from performance_report.matrix_multiplier import MatrixMultiplier


def main():

    # json_file_name = input("Enter the JSON file name: ")
    # image_file_name = input(
    #    "Enter the image file name (e.g., my_bar_chart.png): ")
    BarChartPlotterMultiMatrix.save_bar_chart(
        "res_matrix_multiplier.json", "res_matrix_multiplier.jpg")


if __name__ == '__main__':
    main()
