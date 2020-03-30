"""Run a task multiple times, both inside and outside the Global Interpretar Lock"""
import os
import time
import threading
import multiprocessing

def crunch_numbers():
    """Do some computations"""
    print(f"PID: {os.getpid()}, Process Name: {multiprocessing.current_process().name}, Thread Name: {threading.current_thread().name}")
    x = 0
    while x < 1*10**8:
      x += 1
