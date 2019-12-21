from schedulers import Scheduler
from process import Process
import heapq


class FCFSScheduler(Scheduler):
    process_comparator_key = 'arrival_time'

    def __init__(self):
        super().__init__()
        self.running_queue = []

    def add_process(self, process):
        heapq.heappush(self.running_queue,
                       Process(process=process, comparator_key=self.process_comparator_key))

    def get_active_process(self):
        return None if len(self.running_queue) == 0 else self.running_queue[0]

    def finalize_active_process(self):
        heapq.heappop(self.running_queue)
