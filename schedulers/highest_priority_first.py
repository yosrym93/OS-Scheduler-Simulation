from process import Process
from schedulers import Scheduler
import heapq


class HPFScheduler(Scheduler):
    process_comparator_key = 'priority'

    def __init__(self):
        self.running_queue=[]

    def get_active_process(self):
        return None if len(self.running_queue) == 0 else self.running_queue[0]

    def run_scheduled_process(self):
        process = self.get_active_process()
        if process is not None:
            process.set_preempt_status(False)
        is_running, process_number = super().run_scheduled_process()
        return is_running, process_number

    def finalize_active_process(self):
        heapq.heappop(self.running_queue)

    def add_process(self, process):
        added_process = Process(process=process, comparator_key=self.process_comparator_key)
        # from the second element in the list to the end(Non-Preemptive)
        heapq.heappush(self.running_queue,added_process)
