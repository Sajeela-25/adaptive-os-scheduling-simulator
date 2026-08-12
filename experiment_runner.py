import scheduler
import memory_manager

def run_all_scheduling_tests(processes, quantum=2):

    results = {}

    results["FCFS"] = scheduler.calculate_metrics(
        scheduler.fcfs(processes)
    )

    results["SJF"] = scheduler.calculate_metrics(
        scheduler.sjf(processes)
    )

    results["Priority"] = scheduler.calculate_metrics(
        scheduler.priority_scheduling(processes)
    )

    results["RR"] = scheduler.calculate_metrics(
        scheduler.round_robin(processes, quantum)
    )

    return results


def compare_memory_strategies(blocks, processes_mem):

    return {
        "First Fit": memory_manager.first_fit(blocks.copy(), processes_mem),
        "Best Fit": memory_manager.best_fit(blocks.copy(), processes_mem),
        "Worst Fit": memory_manager.worst_fit(blocks.copy(), processes_mem),
    }