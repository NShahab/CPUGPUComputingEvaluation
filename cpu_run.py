import json
from utils.cpu_operations import cpu_operations
import PlotLineChart
import matplotlib.pyplot as plt
import plot_average_from_json
from image_processing.cpu_image_processing import ImageProcessor


def main():
    # Create an instance of the cpu_operations class
    # cpu_operat = cpu_operations()
    # Perform matrix multiplication on CPU
    # cpu_operat.calculate_and_save_averaged_results()

    # show LineChartPlotter
    # json_filename_cpu = "averaged_execution_cpu_times.json"

    # PlotLineChart.plot_line_chart_from_json(json_filename_cpu)

    # plot_average_from_json.plot_average_from_json('averaged_execution_cpu_times.json', 'averaged_execution_gpu_times.json')

    # -----------image_processing-------------
    # Create an instance of the ImageProcessor class
    image_list = ["data/images/pic1.jpg", "data/images/pic2.jpg",
                  "data/images/pic3.jpg", "data/images/pic4.jpg", "data/images/pic5.jpg"]
    # Create an instance of ImageProcessor
    image_processor = ImageProcessor(image_list)

    # Process images and save results to JSON
    image_processor.process_images()
    # Call the function to plot the image processing performance
    image_processor.plot_image_processing_performance()


if __name__ == '__main__':
    main()
