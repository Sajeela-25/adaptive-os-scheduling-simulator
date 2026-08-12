import threading
import multiprocessing
import time

def thread_task(name):
    time.sleep(2)
    sum(range(1000000))

def process_task(name):
    time.sleep(2)
    sum(range(1000000))

def run_threads():

    threads = []

    start = time.time()

    for i in range(3):

        t = threading.Thread(
            target=thread_task,
            args=(i,)
        )

        threads.append(t)

        t.start()

    for t in threads:
        t.join()

    end = time.time()

    return end - start

def run_processes():

    processes = []

    start = time.time()

    for i in range(3):

        p = multiprocessing.Process(
            target=process_task,
            args=(i,)
        )

        processes.append(p)

        p.start()

    for p in processes:
        p.join()

    end = time.time()

    return end - start