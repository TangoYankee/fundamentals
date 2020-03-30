# Concurrency
Multiple computations are executed during overlapping time periods. This is in contrast to sequentially,
where one computation ends before the next one starts. Concurrent operations may happen in parallel.
However, parallel processes are a distinct because they specifically happen at the same instant. 
Concurrent processes may also utilize time sharing slices, where each computation progresses during its
time slice and is paused otherwise.<sup>1<sup>

## In Python
Within CPython, the Global Interpreter Lock (GIL) implements a mutual exclusion (mutex). The GIL 
simplifies integration with non-thread safe libraries and accelerates sequential computations. However,
it also makes multi-threading impossible within its purview. Fortunately, multi-threading is possible 
in Input/Output operations and libraries such as Python.<sup>2<sup>

## Practice
### Run a task multiple times, both inside and outside the Global Interpretar Lock.<sup>2<sup>

```
import os
import time
import threading
import multiprocessing

NUM_WORKERS = 4

def only_sleep():
    """Do nothing. Wait for a timer to expire"""
    print(f"PID: {os.getpid()}, Process Name: {multiprocessing.current_process().name}, Thread Name: {threading.current_thread().name}")  
    time.sleep(1)

def crunch_numbers():
    """Do some computations"""
    print(f"PID: {os.getpid()}, Process Name: {multiprocessing.current_process().name}, Thread Name: {threading.current_thread().name}")
    x = 0
    while x < 1*10**7:
      x += 1
```

Run ```only_sleep()``` sequentially, multi-threaded, and then with multiple processes.
Compare the results.

```
"""Serial"""
start_time = time.time()
for _ in range(NUM_WORKERS):
    only_sleep()
end_time = time.time()

print(f"Serial time={end_time - start_time}")

"""Threading"""
start_time = time.time()
threads = [threading.Thread(target=only_sleep) of _ in range(NUM_WORKERS)]
[threads.start() for thread in threads]
[threads.join() for thread in threads]
end_time = time.time()

print(f"Threads time={end_time - start_time}")

"""Processes"""
start_time = time.time()
processes = [multiprocessing.Process(target=only_sleep()) for _ in range(NUM_WORKERS)]
[process.start() for process in processes]
[process.join() for process in processes]
end_time = time.time()

print(f"Parallel time={end_time - start_time}")
```

Run ```crunch_numbers()``` sequentially, multi-threaded, and then with multiple processes.
Compare the results.

```
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
processes = [multiprocessing.Process(target=crunch_numbers) for _ in range(NUM_WORKERS)]
[process.start() for process in processes]
[process.join() for process in processes]
end_time = time.time()

print(f"Parallel time={end_time - start_time}")

```

## Sources
1. [wikipedia](https://en.wikipedia.org/wiki/Concurrent_computing)  
2. [tuts plus](https://code.tutsplus.com/articles/introduction-to-parallel-and-concurrent-programming-in-python--cms-28612)

