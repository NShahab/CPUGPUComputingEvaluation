import json
import PlotLineChart
import matplotlib.pyplot as plt
from utils.gpu_operations import gpu_operations
from image_processing.gpu_image_processing import ImageProcessor


def main():

    # Create an instance of the cpu_operations class
    # gpu_ooerat = gpu_operations()

    # Perform matrix multiplication on gpu
    # gpu_ooerat.calculate_and_save_averaged_results()

    # show LineChartPlotter

    # json_filename_gpu = "averaged_execution_gpu_times.json"

    # PlotLineChart.plot_line_chart_from_json(json_filename_gpu)

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
