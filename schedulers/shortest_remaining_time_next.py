from schedulers import Scheduler
import _heapq
from process import Process


class SRTNScheduler(Scheduler):
    process_comparator_key = 'running_time'

    def __init__(self):
        self.running_queue = []

    def run_scheduled_process(self):
        is_running, process_number = super().run_scheduled_process(decrement_comparator=True)
        return is_running, process_number

    def get_active_process(self):
        return None if len(self.running_queue) == 0 else self.running_queue[0]

    def finalize_active_process(self):
        _heapq.heappop(self.running_queue)

    def add_process(self, process):
        _heapq.heappush(self.running_queue, Process(process=process, comparator_key=self.process_comparator_key))
