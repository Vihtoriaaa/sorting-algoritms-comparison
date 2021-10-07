import json
import random
from merge_sort import merge_sort
from selection_sort import selection_sort
from shell_sort import shell_sort
from insertion_sort import insertion_sort
sizes = [128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]


def generate_array(type: str, size: int) -> list:
    """
    Generate and return an array of selected type.
    parameters :
        size - size of array
    type:
        random array | ascending array | descending array | repeated array
    """
    array = [i for i in range(size)]
    if type == "random array":
        return [random.randint(1, 10000) for _ in range(size)]
    elif type == "ascending array":
        return array
    elif type == "descending array":
        return array[::-1]
    elif type == "repeated array":
        return [random.randint(1, 3) for _ in range(size)]


def experiment1(size: int):
    """Creates a list with 5 arrays with random numbers."""
    all_arrays = []
    for _ in range(5):
        arr = generate_array("random array", size)
        all_arrays.append(arr)
    return all_arrays


def experiment2(size: int):
    """Creates a list with an ascending array."""
    all_arrays = []
    all_arrays.append(generate_array("ascending array", size))
    return all_arrays


def experiment3(size: int):
    """Creates a list with a descending array."""
    all_arrays = []
    all_arrays.append(generate_array("descending array", size))
    return all_arrays


def experiment4(size: int):
    """Creates a list with 3 arrays with repeated numbers {1, 2 , 3}."""
    all_arrays = []
    for _ in range(3):
        arr = generate_array("repeated array", size)
        all_arrays.append(arr)
    return all_arrays


def run_experiments():
    """
    Runs all 4 experiments for all types of sorting. Writes a json file with
    sorting type name, experiment done, size of arrays, average time of
    processing the experiment and average number of comparisons performed.
    """
    result = []
    for experiment in (experiment1, experiment2, experiment3, experiment4):
        for size in sizes:
            arrays = experiment(size)
            for sort_type in (selection_sort, insertion_sort, merge_sort, shell_sort):
                total_time, total_comparisons = 0, 0
                for array in arrays:
                    comparisons, work_time = sort_type(array.copy())
                    total_time += work_time
                    total_comparisons += comparisons
                average_time = total_time/len(arrays)
                average_comp = total_comparisons//len(arrays)
                result.append([sort_type.__name__, experiment.__name__, size,
                               average_time, average_comp])

    with open('result.json', 'w') as f:
        json.dump(result, f)


if __name__ == "__main__":
    run_experiments()
