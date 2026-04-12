from process import Process
from monitor import monitor
from scheduler import schedule
from adaptive import adaptive_allocation

# Create processes
processes = [
    Process(1, 5, 100, 3),
    Process(2, 3, 80, 1),
    Process(3, 4, 60, 2)
]

# Simulation loop
for time in range(10):
    print(f"\n--- Time {time} ---")

    # Monitor system
    monitor(processes)

    # Select process to run
    current = schedule(processes)
    print(f"Running Process {current.pid}")

    # Execute process
    current.cpu_burst -= 1

    # Update waiting time
    for p in processes:
        if p != current:
            p.waiting_time += 1

    # Apply adaptive logic
    adaptive_allocation(processes)
