"""Run a task multiple times, both inside and outside the Global Interpretar Lock"""
import os
import time
import threading
import multiprocessing

NUM_WORKERS = 4


def crunch_numbers():
    """Do some computations"""
    print(f"PID: {os.getpid()}, Process Name: {multiprocessing.current_process().name}, Thread Name: {threading.current_thread().name}")
    x = 0
    while x < 1*10**7:
        x += 1


"""Run crunch_numbers() sequentially, multi-threaded, and then with multiple processes.
Compare the results."""

"""Serial"""
start_time = time.time()
for _ in range(NUM_WORKERS):
    crunch_numbers()
end_time = time.time()
print(f"Serial time={end_time - start_time}")

"""Threading"""
start_time = time.time()
threads = [threading.Thread(target=crunch_numbers) for _ in range(NUM_WORKERS)]
[thread.start() for thread in threads]
[thread.join() for thread in threads]
end_time = time.time()

print(f"Threads time={end_time - start_time}")

"""Processes"""
start_time = time.time()
processes = [multiprocessing.Process(
    target=crunch_numbers) for _ in range(NUM_WORKERS)]
[process.start() for process in processes]
[process.join() for process in processes]
end_time = time.time()

print(f"Parallel time={end_time - start_time}")
