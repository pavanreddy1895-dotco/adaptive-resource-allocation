def monitor(processes):
    cpu_usage = sum(p.cpu_burst for p in processes if p.cpu_burst > 0)
    memory_usage = sum(p.memory for p in processes)

    print("\n--- System Monitoring ---")
    print(f"CPU Usage: {cpu_usage}")
    print(f"Memory Usage: {memory_usage}")
