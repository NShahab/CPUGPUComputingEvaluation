import psutil


def get_cpu_usage():
    cpu_percentages = psutil.cpu_percent(percpu=True)
    cpu_count = psutil.cpu_count()

    cores = []
    for i in range(cpu_count):
        core = {
            'core_number': i + 1,
            'usage_percentage': cpu_percentages[i]
        }
        cores.append(core)

    return cores
