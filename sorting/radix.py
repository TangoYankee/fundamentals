"""Source:
https://en.wikibooks.org/wiki/Algorithm_Implementation/Sorting/Radix_sort"""

from time import time as current_time
from random import randint


def radix_sort(a, n, maxLen):
    for x in range(maxLen):
        bins = [[] for i in range(n)]
        for y in a:
            bins[int(y/n**x) % n].append(y)
        a = []
        for section in bins:
            a.extend(section)
    return a


def compare_sorts(data, n, maxLen):
    start_time = current_time()
    radix_sort(data, n, maxLen)
    print(f"Radix time: { current_time() - start_time}")
    start_time = current_time()
    sorted(data)
    print(f"Tim Sort time: {current_time() - start_time}")


def main():
    compare_sorts([randint(0, 100) for _ in range(10)], 9, 3)
    # Radix time: 2.9087066650390625e-05
    # Tim Sort time: 3.5762786865234375e-06
    compare_sorts([randint(0, 100) for _ in range(10**4)], 10**6-1, 3)
    # Radix time: 1.0376839637756348
    # Tim Sort time: 0.0019342899322509766


if __name__ == "__main__":
    main()
