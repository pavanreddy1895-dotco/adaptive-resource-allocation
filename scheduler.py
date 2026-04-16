def schedule(processes):
    processes.sort(key=lambda x: x.priority)
    return processes[0]