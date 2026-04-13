# Adaptive-Resource-Allocation
Develop a system that dynamically adjusts resource allocation among multiple programs to optimize CPU and memory utilization. The solution should monitor system performance and reallocate resources in real-time to prevent bottlenecks.
Team Members
# Beedala Pavan Kumar Reddy
# Irugula Karthikeya Reddy
# Apoorav Thakur
## Description
This project simulates a multiprogramming system where CPU and memory resources are allocated dynamically. The system monitors performance and adjusts process priorities in real-time to avoid bottlenecks and ensure fairness.

## Features
- Dynamic CPU scheduling
- Memory usage monitoring
- Adaptive priority adjustment
- Starvation prevention
- Real-time system simulation

## Project Structure
- process.py → Defines process attributes
- monitor.py → Tracks CPU and memory usage
- scheduler.py → Selects process to execute
- adaptive.py → Adjusts priorities dynamically
- main.py → Integrates all modules

## How to Run
1. Open terminal in project folder
2. Run:
   python main.py

## Sample Output
The system prints:
- CPU usage
- Memory usage
- Currently running process at each time step
