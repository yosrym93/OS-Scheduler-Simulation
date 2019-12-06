class Process:
    def __init__(self, process, comparator_key='arrival_time'):
        self.number = process['number']
        self.priority = process['priority']
        self.running_time = process['running_time']
        self.arrival_time = process['arrival_time']
        self.comparator = process[comparator_key]
        self.preempt_status = True

    def __lt__(self, other):
        # If the other process has preempt status == false therefore don't preempt
        if other.preempt_status:
            if self.comparator == other.comparator:
                return self.number < other.number
            else:
                return self.comparator < other.comparator
        else:
            return False

    def __repr__(self):
        return "Process number: {0}, Arrival Time: {1}, Burst Time: {2}, Priority: {3}".format(
            self.number, self.arrival_time, self.running_time, self.priority
        )

    def set_preempt_status(self, status):
        self.preempt_status = status
