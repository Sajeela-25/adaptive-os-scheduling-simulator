def first_fit(blocks, processes):
    allocation = [-1] * len(processes)
    blocks = blocks.copy()

    for i in range(len(processes)):
        for j in range(len(blocks)):
            if blocks[j] >= processes[i]:
                allocation[i] = j
                blocks[j] -= processes[i]
                break

    return allocation


def best_fit(blocks, processes):
    allocation = [-1] * len(processes)
    blocks = blocks.copy()

    for i in range(len(processes)):
        best_idx = -1

        for j in range(len(blocks)):
            if blocks[j] >= processes[i]:
                if best_idx == -1 or blocks[j] < blocks[best_idx]:
                    best_idx = j

        if best_idx != -1:
            allocation[i] = best_idx
            blocks[best_idx] -= processes[i]

    return allocation


def worst_fit(blocks, processes):
    allocation = [-1] * len(processes)
    blocks = blocks.copy()

    for i in range(len(processes)):
        worst_idx = -1

        for j in range(len(blocks)):
            if blocks[j] >= processes[i]:
                if worst_idx == -1 or blocks[j] > blocks[worst_idx]:
                    worst_idx = j

        if worst_idx != -1:
            allocation[i] = worst_idx
            blocks[worst_idx] -= processes[i]

    return allocation


def paging(process_sizes, frame_size):
    """
    Paging simulation: returns number of pages per process
    """
    if frame_size <= 0:
        return [0 for _ in process_sizes]

    return [
        (size + frame_size - 1) // frame_size
        for size in process_sizes
    ]


def fragmentation(blocks):
    """
    External fragmentation analysis
    """
    if not blocks:
        return {
            "total_free": 0,
            "largest_block": 0,
            "external_fragmentation": 0
        }

    total_free = sum(blocks)
    largest_block = max(blocks)
    external_fragmentation = total_free - largest_block

    return {
        "total_free": total_free,
        "largest_block": largest_block,
        "external_fragmentation": external_fragmentation
    }