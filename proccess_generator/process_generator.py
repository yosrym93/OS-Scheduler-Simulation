import numpy as np


def adjust_time(time):
    return abs(int(time))


if __name__ == '__main__':
    input_file = open('processes_parameters.txt')
    output_file = open('processes.txt', 'w')
    processes_count, arrival_time_mean, arrival_time_std, \
        burst_time_mean, burst_time_std, priority_lambda = [float(x) for x in input_file.read().split()]

    processes_count = int(processes_count)
    output_file.write(str(processes_count) + '\n')

    for i in range(1, processes_count + 1):
        arrival_time = adjust_time(np.random.normal(arrival_time_mean, arrival_time_std))
        burst_time = adjust_time(np.random.normal(burst_time_mean, burst_time_std))
        priority = adjust_time(np.random.poisson(priority_lambda))
        output_file.write('{0} {1} {2} {3}'.format(
            i, arrival_time, burst_time, priority))
        output_file.write('\n')
