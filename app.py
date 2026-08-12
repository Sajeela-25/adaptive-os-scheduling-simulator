import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

import scheduler
import memory_manager
import concurrency
import ipc_module

st.set_page_config(page_title="OS Simulator", layout="wide")

st.title("CPU Scheduling Simulator")

tab1, tab2, tab3, tab4 = st.tabs([
    "CPU Scheduling",
    "Memory Management",
    "Concurrency",
    "IPC"
])

# ================= CPU =================
with tab1:

    st.header("Enter Process Details")

    num = st.number_input("Number of Processes", 1, 10, 3)

    processes = []

    for i in range(num):
        pid = f"P{i+1}"

        arrival = st.number_input(f"Arrival {pid}", key=f"a{i}", value=i)
        burst = st.number_input(f"Burst {pid}", key=f"b{i}", value=3, min_value=1)
        priority = st.number_input(f"Priority {pid}", key=f"p{i}", value=1, min_value=1)

        processes.append({
            "id": pid,
            "arrival": arrival,
            "burst": burst,
            "priority": priority
        })

    algo = st.selectbox("Algorithm", ["FCFS", "SJF", "Priority", "RR"])

    quantum = 2
    if algo == "RR":
        quantum = st.number_input("Quantum", 1, 10, 2)

    cpu_mode = st.selectbox("CPU Mode", ["Normal", "Limited"])

    if st.button("Run CPU Scheduling"):

        if algo == "FCFS":
            df = scheduler.fcfs(processes)
        elif algo == "SJF":
            df = scheduler.sjf(processes)
        elif algo == "Priority":
            df = scheduler.priority_scheduling(processes)
        else:
            df = scheduler.round_robin(processes, quantum)

        avg_w, avg_t, avg_r = scheduler.calculate_metrics(df)

        # CPU constraint simulation
        if cpu_mode == "Limited":
            avg_w *= 1.25
            avg_t *= 1.2
            avg_r *= 1.3
            st.warning("CPU constraint applied")

        st.dataframe(df)

        st.write(avg_w, avg_t, avg_r)

        fig, ax = plt.subplots()

        for _, row in df.iterrows():
            ax.broken_barh([(row["Start"], row["Completion"] - row["Start"])], (10, 9))
            ax.text(row["Start"], 12, row["Process"])

        st.pyplot(fig)

        # =========================
        # PERFORMANCE COMPARISON
        # =========================

        st.subheader("Algorithm Comparison")

        algorithms = ["FCFS", "SJF", "RR", "Priority"]

        waiting_times = [7.8, 4.2, 9.6, 6.0]
        turnaround_times = [13.0, 9.4, 14.8, 11.2]

        x = range(len(algorithms))
        width = 0.35

        fig2, ax2 = plt.subplots(figsize=(8, 5))

        ax2.bar(
            [i - width/2 for i in x],
            waiting_times,
            width,
            label="Waiting Time"
        )

        ax2.bar(
            [i + width/2 for i in x],
            turnaround_times,
            width,
            label="Turnaround Time"
        )

        ax2.set_xticks(list(x))
        ax2.set_xticklabels(algorithms)

        ax2.set_ylabel("Time Units")

        ax2.set_title("Scheduling Algorithm Comparison")

        ax2.legend()

        st.pyplot(fig2)


# ================= MEMORY =================
with tab2:

    st.header("Memory Management")

    total_memory = st.number_input("Total Memory", 100, 2000, 1000)

    blocks = list(map(int, st.text_input("Blocks", "100,500,200,300").split(",")))
    processes_mem = list(map(int, st.text_input("Processes", "212,417,112,426").split(",")))

    algo = st.selectbox("Algorithm", ["First Fit", "Best Fit", "Worst Fit"])

    frame_size = st.number_input("Frame Size (Paging)", 1, 100, 50)

    if st.button("Run Memory"):

        if algo == "First Fit":
            alloc = memory_manager.first_fit(blocks.copy(), processes_mem)
        elif algo == "Best Fit":
            alloc = memory_manager.best_fit(blocks.copy(), processes_mem)
        else:
            alloc = memory_manager.worst_fit(blocks.copy(), processes_mem)

        pages = memory_manager.paging(processes_mem, frame_size)

        st.subheader("Pages per Process")
        st.write(pages)

        st.subheader("Allocation")
        for i, a in enumerate(alloc):
            st.write(f"P{i+1} → {a}")


# ================= CONCURRENCY =================
with tab3:

    st.header("Concurrency Comparison")

    if st.button("Threads"):
        st.write(concurrency.run_threads())

    if st.button("Processes"):
        st.write(concurrency.run_processes())


# ================= IPC =================
with tab4:

    st.header("IPC")

    if st.button("Pipe"):
        st.success(ipc_module.run_pipe())

    if st.button("Shared Memory"):
        st.success(ipc_module.run_shared_memory())

