def write_stats(statistics):
    output_file = open('statistics.txt', 'w')
    processes_count = len(statistics)
    statistics = sorted(statistics, key=lambda k: k.number)
    output_file.write("Process Number " +"\t Waiting time" + "\t Turn around"+ "\t Weighted turn around"+'\n')
    sum_weighted = sum_ta = 0
    for i in range(0, processes_count):
        output_file.write('{0}  \t\t\t{1}  \t\t{2}  \t\t{3}'.format(
            statistics[i].number, statistics[i].waiting_time, statistics[i].turnaround,
            "{0:.2f}".format(statistics[i].weighted_turnaround)))
        output_file.write('\n')
        sum_weighted += statistics[i].weighted_turnaround
        sum_ta += statistics[i].turnaround
    output_file.write("Average Turn Around" + "\t" + "{0:.2f}".format(sum_ta/processes_count) + '\n')
    output_file.write("Average Weighted Turn Around" + "\t" + "{0:.2f}".format(sum_weighted/processes_count) + '\n')
