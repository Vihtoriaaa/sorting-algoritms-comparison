import time
import random
arr = [random.randint(0, 100000) for _ in range(32768)]


def selection_sort(num_list):
    """Implementation of selection sort."""
    start = time.time()
    counter = 0
    for items in range(len(num_list)-1, 0, -1):
        max_pos = 0
        for item in range(1, items+1):
            if num_list[max_pos] < num_list[item]:
                max_pos = item
            counter += 1
        temp = num_list[max_pos]
        num_list[max_pos] = num_list[item]
        num_list[item] = temp
    return counter, time.time() - start


