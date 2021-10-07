import time
import random
arr = [random.randint(0, 100000) for _ in range(32768)]


def shell_sort(arr):
    """Implementation of shell sort."""
    counter = 0
    start = time.time()
    sublistCount = int(len(arr)/2)
    while sublistCount > 0:
        for start_idx in range(sublistCount):
            counter += do_insertsort_gap(arr, start_idx, sublistCount)
        sublistCount = int(sublistCount/2)
    return counter, time.time() - start


def do_insertsort_gap(arr, start, gap):
    """Creating gaps for shell sort."""
    counter = 0
    for i in range(start+gap, len(arr), gap):
        currentValue = arr[i]
        position = i
        counter += 1
        while position >= gap and arr[position-gap] >= currentValue:
            arr[position] = arr[position-gap]
            position = position-gap
        arr[position] = currentValue
    return counter

