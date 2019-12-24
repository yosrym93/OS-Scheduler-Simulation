from schedulers import Scheduler
from process import Process
from collections import deque


# Assumptions:
# Context switch ONLY when a running process is replaced with another, if a process finished no context switch
# If a process arrives at the same time another one finishes, insert the new one in the queue first
# If a process finished a quantum with no other processes existing, give it a full new quantum
class RoundRobinScheduler(Scheduler):
    def __init__(self, quantum_length, context_switch_length):
        super().__init__()
        self.running_queue = deque([])
        self.quantum_length = quantum_length
        self.current_quantum_state = quantum_length
        self.context_switch_length = context_switch_length
        self.current_context_switch_state = 0

    def run_scheduled_process(self, current_time):
        if self.current_quantum_state == 0:
            self.current_quantum_state = self.quantum_length
            self.current_context_switch_state = self.context_switch_length
            self.running_queue.rotate()
        if self.current_context_switch_state > 0:
            self.current_context_switch_state -= 1
            return True, None
        is_running, process_number = super().run_scheduled_process(current_time=current_time)
        if len(self.running_queue) > 0:
            self.current_quantum_state -= 1
        return is_running, process_number

    def add_process(self, process):
        self.running_queue.appendleft(Process(process))

    def get_active_process(self):
        return None if len(self.running_queue) == 0 else self.running_queue[-1]

    def finalize_active_process(self):
        self.running_queue.pop()
        self.current_quantum_state = self.quantum_length
        if len(self.running_queue) > 0:
            self.current_quantum_state += 1  # Add 1 as it will be decremented
