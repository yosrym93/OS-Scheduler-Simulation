import matplotlib.pyplot as plt


def plot_graph(times, scheduled_processes, context_switches, xticks, processes_count):
    ax = plt.subplot(111)
    ax.bar(times, scheduled_processes, width=1, color='b', align='edge')
    ax.bar(context_switches, 0.5, width=1, color='r', align='edge')
    ax.set_xticks(ticks=xticks)
    ax.set_yticks(ticks=range(processes_count + 1))
    ax.set_xlabel('Time')
    ax.set_ylabel('Scheduled Process')
    ax.set_xlim(left=0)
    plt.show()
