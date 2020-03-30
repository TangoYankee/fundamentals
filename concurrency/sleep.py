"""Run a task multiple times, both inside and outside the Global Interpretar Lock"""
import os
import time
import threading
import multiprocessing

NUM_WORKERS = 4

def only_sleep():
    """Do nothing. Wait for a timer to expire"""
    print(f"PID: {os.getpid()}, Process Name: {multiprocessing.current_process().name}, Thread Name: {threading.current_thread().name}")  
    time.sleep(1)

"""Run only_sleep() sequentially, multi-threaded, and then with multiple processes. Compare the results."""
"""Serial"""
start_time = time.time()
for _ in range(NUM_WORKERS):
    only_sleep()
end_time = time.time()

print(f"Serial time={end_time - start_time}")

"""Threading"""
start_time = time.time()
threads = [threading.Thread(target=only_sleep) for _ in range(NUM_WORKERS)] # mistake: wrote 'of' instead of 'for'
[thread.start() for thread in threads] # mistake: tried to operation on the list, rather than the item (threads/thread)
[thread.join() for thread in threads] 
end_time = time.time()

print(f"Threads time={end_time - start_time}")

"""Processes"""
start_time = time.time()
processes = [multiprocessing.Process(target=only_sleep) for _ in range(NUM_WORKERS)] # Mistake: invoked time_sleep function, instead of referencing it.
[process.start() for process in processes]
[process.join() for process in processes]
end_time = time.time()

print(f"Parallel time={end_time - start_time}")
