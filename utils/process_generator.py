import numpy as np

input_file = open('processes_parameters.txt')
output_file = open('processes.txt', 'w')
processes_count, arrival_time_mean, arrival_time_std, \
    burst_time_mean, burst_time_std, priority_lambda = [float(x) for x in input_file.read().split()]

processes_count = int(processes_count)
output_file.write(str(processes_count) + '\n')
for i in range(1, processes_count + 1):
    arrival_time = np.random.normal(arrival_time_mean, arrival_time_std)
    burst_time = np.random.normal(burst_time_mean, burst_time_std)
    priority = np.random.poisson(priority_lambda)
    output_file.write('{0} {1} {2} {3}'.format(
        i, round(arrival_time), round(burst_time), round(priority)))
    output_file.write('\n')
