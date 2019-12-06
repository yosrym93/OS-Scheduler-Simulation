from utils import read_processes, plot_graph
from schedulers import FCFSScheduler, RoundRobinScheduler


def is_context_switch(scheduled_process):
    return scheduled_process == -1


if __name__ == '__main__':
    processes = read_processes('processes.txt')    # TODO Use CLI to get input file path
    processes = sorted(processes, key=lambda p: (p['arrival_time'], p['number']), reverse=True)
    processes_count = len(processes)

    scheduler = RoundRobinScheduler(quantum_length=4, context_switch_length=1)     # TODO Use CLI to decide the scheduler type
    scheduled_processes = []
    context_switches = []
    process_switches = []  # The times where the process changes, used to tick X-axis on the bar chart
    time = 0
    next_process = None if len(processes) == 0 else processes[-1]
    while True:
        # Add arriving processes to the scheduler
        while next_process is not None and next_process['arrival_time'] == time:
            process = processes.pop()
            scheduler.add_process(process)
            next_process = None if len(processes) == 0 else processes[-1]

        # Run the scheduled process
        is_running, current_process = scheduler.run_scheduled_process()
        # Check for termination case (no more arriving processes & scheduler idle)
        if not is_running and next_process is None:
            process_switches.append(time)
            break
        # Check if context switch or running process
        if is_context_switch(current_process):
            context_switches.append(time)
            scheduled_processes.append(0)
        else:
            scheduled_processes.append(current_process)
        # Record the times at which the graph changes
        if time > 0 and current_process != scheduled_processes[time - 1]:
            process_switches.append(time)
        time += 1

    plot_graph(times=range(time),
               scheduled_processes=scheduled_processes,
               context_switches=context_switches,
               xticks=process_switches,
               processes_count=processes_count)
