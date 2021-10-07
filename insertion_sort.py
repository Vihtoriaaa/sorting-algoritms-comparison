import time
import random
arr = [random.randint(0, 100000) for _ in range(32768)]


def insertion_sort(num_list):
    """Implementation of insertion sort."""
    counter = 0
    start = time.time()
    for num in range(1, len(num_list)):
        cur_val = num_list[num]
        pos = num
        counter += 1
        while pos > 0 and num_list[pos-1] > cur_val:
            num_list[pos] = num_list[pos-1]
            pos -= 1
            counter += 1
        num_list[pos] = cur_val
    return counter, time.time() - start
