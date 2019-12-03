from utils.process_reader import read_processes
from schedulers.base_scheduler import Scheduler


if __name__ == '__main__':
    processes = read_processes('processes.txt')    # TODO Use GUI to get input file path
    processes = sorted(processes, key=lambda p: p['arrival_time'], reverse=True)

    scheduler = Scheduler()     # Replace with scheduler type (TODO Use GUI to decide the scheduler type)
    time = 0
    process_scheduling_table = []
    next_process = processes[-1]
    while True:
        while next_process is not None and next_process['arrival_time'] == time:
            process = processes.pop()
            scheduler.add_process(process)
            next_process = processes[-1]

        is_running, current_process = scheduler.run_scheduled_process()
        if not is_running and next_process is None:
            break
        process_scheduling_table.append((time, current_process))
        time += 1

    print(process_scheduling_table)  # TODO Plot the table as a graph
