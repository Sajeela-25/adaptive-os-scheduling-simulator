import pandas as pd

def fcfs(processes):
    processes = sorted(processes, key=lambda x: x['arrival'])
    current_time = 0
    result = []

    for p in processes:
        if current_time < p['arrival']:
            current_time = p['arrival']

        start = current_time
        completion = start + p['burst']

        waiting = start - p['arrival']
        turnaround = completion - p['arrival']
        response = waiting

        result.append({
            'Process': p['id'],
            'Start': start,
            'Completion': completion,
            'Waiting': waiting,
            'Turnaround': turnaround,
            'Response': response
        })

        current_time = completion

    return pd.DataFrame(result)


def sjf(processes):
    processes = sorted(processes, key=lambda x: (x['arrival'], x['burst']))
    completed = []
    current_time = 0
    ready = []

    while processes or ready:
        while processes and processes[0]['arrival'] <= current_time:
            ready.append(processes.pop(0))

        if ready:
            ready.sort(key=lambda x: x['burst'])
            p = ready.pop(0)

            start = current_time
            completion = start + p['burst']

            completed.append({
                'Process': p['id'],
                'Start': start,
                'Completion': completion,
                'Waiting': start - p['arrival'],
                'Turnaround': completion - p['arrival'],
                'Response': start - p['arrival']
            })

            current_time = completion
        else:
            current_time += 1

    return pd.DataFrame(completed)


def priority_scheduling(processes):
    processes = sorted(processes, key=lambda x: (x['arrival'], x['priority']))
    return fcfs(processes)


def round_robin(processes, quantum=2):
    queue = processes.copy()
    time = 0
    remaining = {p['id']: p['burst'] for p in queue}
    first_response = {}
    result = []

    while queue:
        p = queue.pop(0)

        if time < p['arrival']:
            time = p['arrival']

        if p['id'] not in first_response:
            first_response[p['id']] = time - p['arrival']

        run_time = min(quantum, remaining[p['id']])
        start = time
        time += run_time
        remaining[p['id']] -= run_time

        result.append({
            'Process': p['id'],
            'Start': start,
            'Completion': time
        })

        if remaining[p['id']] > 0:
            queue.append(p)

    final = []
    for p in processes:
        completion = max([x['Completion'] for x in result if x['Process'] == p['id']])
        turnaround = completion - p['arrival']
        waiting = turnaround - p['burst']

        final.append({
            'Process': p['id'],
            'Start': next(x['Start'] for x in result if x['Process'] == p['id']),
            'Completion': completion,
            'Waiting': waiting,
            'Turnaround': turnaround,
            'Response': first_response[p['id']]
        })

    return pd.DataFrame(final)


def calculate_metrics(df):
    avg_waiting = df['Waiting'].mean()
    avg_turnaround = df['Turnaround'].mean()
    avg_response = df['Response'].mean()

    return avg_waiting, avg_turnaround, avg_response