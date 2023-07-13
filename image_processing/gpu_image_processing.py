import cv2
import time
import json
import os
import matplotlib.pyplot as plt
import json


class ImageProcessor:
    def __init__(self, image_list):
        self.image_list = image_list

    def gpu_image_processing(self, image):
        start_time = time.time()

        # Perform image processing operations using GPU
        gpu_image = cv2.cuda_GpuMat()
        gpu_image.upload(image)
        gpu_gray_image = cv2.cuda.cvtColor(gpu_image, cv2.COLOR_BGR2GRAY)
        gray_image = gpu_gray_image.download()

        end_time = time.time()
        execution_time = end_time - start_time
        return gray_image, execution_time

    def process_images(self):
        results = []
        for image_path in self.image_list:
            image = cv2.imread(image_path)
            gpu_result, gpu_execution_time = self.gpu_image_processing(image)

            # Get the image size instead of the actual image data
            image_size = os.path.getsize(image_path)

            result = {
                'image_path': image_path,
                'image_size': image_size,
                'gpu_execution_time': gpu_execution_time
            }
            results.append(result)

        # Save results to a JSON file
        with open('img-proc-gpu.json', 'w') as file:
            json.dump(results, file)

    def plot_image_processing_performance(self):
        # Load data from JSON file
        with open('img-proc-gpu.json', 'r') as file:
            results = json.load(file)

        # Extract required information for plotting
        image_sizes = [result['image_size'] for result in results]
        execution_times = [result['cpu_execution_time'] for result in results]

        # Plotting the line chart
        plt.plot(image_sizes, execution_times)
        plt.xlabel('Image Size (bytes)')
        plt.ylabel('Execution Time (seconds)')
        plt.title('GPU Image Processing Performance')
        plt.tight_layout()
        plt.savefig("img-proc-gpu.png")
        # Display the line chart
        plt.show()
