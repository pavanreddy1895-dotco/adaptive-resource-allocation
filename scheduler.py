def schedule(processes):
    # Sort processes based on priority (lower value = higher priority)
    processes.sort(key=lambda x: x.priority)

    # Select the highest priority process
    current_process = processes[0]

    return current_process
