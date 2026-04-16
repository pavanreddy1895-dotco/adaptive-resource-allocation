def adaptive_allocation(processes):
    for p in processes:
        if p.waiting_time > 2:
            p.priority = max(1, p.priority - 1)