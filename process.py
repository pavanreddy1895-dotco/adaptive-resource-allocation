# Process class module
class Process:
    def __init__(self, pid, cpu_burst, memory, priority):
        self.pid = pid
        self.cpu_burst = cpu_burst
        self.memory = memory
        self.priority = priority

        self.waiting_time = 0

        self.waiting_time = 0

