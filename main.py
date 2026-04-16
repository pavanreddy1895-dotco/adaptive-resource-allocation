from process import Process
from monitor import monitor
from scheduler import schedule
from adaptive import adaptive_allocation

processes = [
    Process(1, 5, 100, 3),
    Process(2, 3, 80, 1),
    Process(3, 4, 60, 2)
]

for t in range(10):
    print("\nTime:", t)

    monitor(processes)

    current = schedule(processes)
    print("Running Process", current.pid)

    current.cpu_burst -= 1

    for p in processes:
        if p != current:
            p.waiting_time += 1

    adaptive_allocation(processes)