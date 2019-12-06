from process import Process
from schedulers import Scheduler
import heapq


class HPFScheduler(Scheduler):
    process_comparator_key = 'priority'

    def __init__(self):
        self.running_queue=[]

    def get_active_process(self):
        return None if len(self.running_queue) == 0 else self.running_queue[0]

    def finalize_active_process(self):
        heapq.heappop(self.running_queue)
        if len(self.running_queue) != 0:
            self.running_queue[0].set_preempt_status(False)

    def add_process(self, process):
        added_process = Process(process=process, comparator_key=self.process_comparator_key)
        if len(self.running_queue) == 0:
            added_process.set_preempt_status(False)
        # from the second element in the list to the end(Non-Preemptive)
        heapq.heappush(self.running_queue,added_process)
