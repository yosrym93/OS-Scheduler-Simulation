from abc import ABC, abstractmethod


class Scheduler(ABC):
    def __init__(self):
        self.statistics = []

    def run_scheduled_process(self, current_time, decrement_comparator=False):
        # Run the scheduled process for 1 time step
        process = self.get_active_process()
        if process is None:
            return False, 0
        process.running_time -= 1
        if decrement_comparator:
            process.comparator -= 1
        if process.running_time == 0:
            self.finalize_active_process()
            process.finalize_stats(current_time)
            self.statistics.append(process)
        return True, process.number

    @abstractmethod
    def add_process(self, process):
        pass

    @abstractmethod
    def get_active_process(self):
        pass

    @abstractmethod
    def finalize_active_process(self):
        pass

    def return_stats(self):
        return self.statistics

