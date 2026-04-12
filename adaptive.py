def adaptive_allocation(processes):
    for p in processes:
        # If a process is waiting too long, increase its priority
        if p.waiting_time > 2:
            p.priority = max(1, p.priority - 1)

        # If a process is using too much CPU, reduce its priority
        if p.cpu_burst > 5:
            p.priority += 1
