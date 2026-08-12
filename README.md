# Adaptive OS Scheduling & Resource Management Simulator

## Overview

An interactive Operating Systems simulator built with **Python and Streamlit** to demonstrate CPU scheduling, memory management, concurrency, IPC, and Docker-based resource management.

## Features

- CPU Scheduling:
  - FCFS
  - SJF
  - Priority Scheduling
  - Round Robin
- Waiting, Turnaround & Response Time
- Gantt Chart Visualization
- Adaptive Scheduling Feedback
- Memory Management:
  - First Fit
  - Best Fit
  - Memory Utilization
  - Fragmentation Analysis
- Concurrency:
  - Multithreading
  - Multiprocessing
- IPC:
  - Pipes
  - Shared Memory
- Docker Containerization
- CPU & Memory Resource Limits
- Docker Process Isolation
- Performance Comparison

## Technologies

- Python 3.11
- Streamlit
- Pandas
- Matplotlib
- Docker
- Multiprocessing
- Threading

## Project Structure

```text
adaptive-os-scheduling-simulator/
│
├── app.py
├── scheduler.py
├── memory_manager.py
├── concurrency.py
├── ipc_module.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
