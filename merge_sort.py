import time
import random
arr = [random.randint(0, 100000) for _ in range(32768)]


def merge_sort(num_list):
    """Implementation of merge sort."""
    start = time.time()
    counter = 0
    if len(num_list) > 1:
        middle = len(num_list)//2
        left_part = num_list[:middle]
        right_part = num_list[middle:]
        counter += merge_sort(left_part)[0]
        counter += merge_sort(right_part)[0]
        i, j, k = 0, 0, 0

        while i < len(left_part) and j < len(right_part):
            if left_part[i] < right_part[j]:
                num_list[k] = left_part[i]
                i += 1
            else:
                num_list[k] = right_part[j]
                j += 1
            k += 1
            counter += 1

        while i < len(left_part):
            num_list[k] = left_part[i]
            i += 1
            k += 1
            counter += 1

        while j < len(right_part):
            num_list[k] = right_part[j]
            j += 1
            k += 1
            counter += 1
    return counter, time.time() - start
