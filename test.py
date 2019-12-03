from utils.process_reader import read_processes
from process.process import Process
import heapq

# Free experimentation area
# Comment existing tests before writing yours

priority_queue = []
processes = read_processes('output.txt')
processes = [Process(p, 'arrival_time') for p in processes]
for p in processes:
    heapq.heappush(priority_queue, p)

for i in range(len(priority_queue)):
    print(heapq.heappop(priority_queue))
