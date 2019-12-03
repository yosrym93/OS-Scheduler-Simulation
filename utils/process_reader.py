def read_processes(filename):
    input_file = open(filename)
    processes_count = int(input_file.readline().split()[0])
    processes = []

    for i in range(processes_count):
        process = dict()
        process['number'], process['arrival_time'], process['running_time'], process['priority'] = \
            [int(x) for x in input_file.readline().split()]
        processes.append(process)

    return processes
