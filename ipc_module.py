from multiprocessing import Pipe, Process, Value

# =========================
# PIPE IPC
# =========================

def sender(conn):

    conn.send("Scheduling Data Sent Successfully")

    conn.close()

def run_pipe():

    parent_conn, child_conn = Pipe()

    p = Process(
        target=sender,
        args=(child_conn,)
    )

    p.start()

    message = parent_conn.recv()

    p.join()

    return message

# =========================
# SHARED MEMORY IPC
# =========================

def shared_memory_task(shared_value):

    shared_value.value = 50

def run_shared_memory():

    shared_value = Value('i', 0)

    p = Process(
        target=shared_memory_task,
        args=(shared_value,)
    )

    p.start()

    p.join()

    return shared_value.value

# =========================
# TEST SECTION
# =========================

if __name__ == "__main__":

    print(run_pipe())

    print(run_shared_memory())