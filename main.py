import json
from utils.cpu_operations import cpu_operations
#from utils.gpu_operations import gpu_operations
import BarChartPlotter
import PlotLineChart
import matplotlib.pyplot as plt
import plot_average_from_json
import utils.Scenario2 


def main():
    # cpu=1  and gpu=2


 
    # Create an instance of the cpu_operations class
    #cpu_operat = cpu_operations()
    # Perform matrix multiplication on CPU
    #cpu_operat.calculate_and_save_averaged_results()

    # show LineChartPlotter
    #json_filename_cpu = "averaged_execution_cpu_times.json"
    
    #PlotLineChart.plot_line_chart_from_json(json_filename_cpu)
   
    plot_average_from_json.plot_average_from_json('averaged_execution_cpu_times.json', 'averaged_execution_gpu_times.json')


    # Create an instance of the cpu_operations class
    #gpu_ooerat = gpu_operations()
   
    # Perform matrix multiplication on gpu
    #gpu_ooerat.calculate_and_save_averaged_results()    

    # show LineChartPlotter
    
    #json_filename_gpu = "averaged_execution_gpu_times.json"
   
    #PlotLineChart.plot_line_chart_from_json(json_filename_gpu)

if __name__ == '__main__':
    main()