import json
import matplotlib.pyplot as plt


def save_bar_chart(json_file_name, image_file_name):
    # Open the JSON file and load the data
    with open(json_file_name, 'r') as json_file:
        data = json.load(json_file)

    # Extract the results
    parallel_result = data['Parallel multiplication result']
    serial_result = data['Serial multiplication result']
    parallel_time = data['Parallel multiplication time']
    serial_time = data['Serial multiplication time']

    # Generate the bar chart
    fig, ax = plt.subplots()

    # Set values for the bars
    bar_labels = ['Parallel', 'Serial']
    bar_values = [parallel_time, serial_time]

    # Plot the bar chart
    ax.bar(bar_labels, bar_values)

    # Title and axes labels
    ax.set_title('Matrix Multiplication Results')
    ax.set_xlabel('Method')
    ax.set_ylabel('Result')

    # Save the chart as an image with the specified file name
    plt.show()
    plt.savefig(image_file_name)
