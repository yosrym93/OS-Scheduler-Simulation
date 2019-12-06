import click
from utils import read_processes, plot_graph
from schedulers import FCFSScheduler, RoundRobinScheduler, HPFScheduler, SRTNScheduler


@click.command()
@click.option('-f', '--file', default='hpfprocesses.txt',
              help='Input file with processes data.')
@click.option('-s', '--scheduler', type=click.Choice(['rr', 'fcfs', 'srtn', 'hpf']),
              help='Scheduler type.', required=True,default = 'srtn')
@click.option('-q', '--quantum', default=2, type=click.types.INT,
              help='Quantum length for Round Robin.')
@click.option('-cs', '--context_switch', default=1, type=click.types.INT,
              help='Context Switch Length for Round Robin')
def cli(file, scheduler, quantum, context_switch):
    try:
        processes = read_processes(file)
    except FileNotFoundError:
        print('File not found.')
        return
    processes = sorted(processes, key=lambda p: (p['arrival_time'], p['number']), reverse=True)
    scheduler = create_scheduler(scheduler, quantum, context_switch)
    schedule(processes, scheduler)


def create_scheduler(scheduler, quantum, context_switch):
    if scheduler == 'fcfs':
        return FCFSScheduler()
    elif scheduler == 'rr':
        return RoundRobinScheduler(quantum, context_switch)
    elif scheduler == 'srtn':
        return SRTNScheduler()
    elif scheduler == 'hpf':
        return HPFScheduler()


def schedule(processes, scheduler):
    processes_count = len(processes)
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
        if current_process is None:
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


if __name__ == '__main__':
    cli()
