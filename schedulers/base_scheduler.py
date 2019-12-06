from abc import ABC, abstractmethod


class Scheduler(ABC):
    def run_scheduled_process(self, decrement_comparator=False):
        # Run the scheduled process for 1 time step
        process = self.get_active_process()
        if process is None:
            return False, 0
        process.running_time -= 1
        if decrement_comparator:
            process.comparator -= 1
        if process.running_time == 0:
            self.finalize_active_process()
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
