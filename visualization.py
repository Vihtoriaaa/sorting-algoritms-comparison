import matplotlib.pyplot as plt
import json


results = "sorted_json.json"
experiment = input("Enter name of experiment: ")

plt.title(experiment)
plt.xlabel('Array length (power of 2)')
plt.ylabel("Comparisons")

with open(results, 'r') as results_file:
    data = json.load(results_file)
insertionsort = []
selectionsort = []
mergesort = []
shellsort = []

for power in range(7, 16):
    insertionsort.append(
        data[experiment]["insertion_sort"][str(2 ** power)][1])
    selectionsort.append(
        data[experiment]["selection_sort"][str(2 ** power)][1])
    mergesort.append(data[experiment]["merge_sort"][str(2 ** power)][1])
    shellsort.append(data[experiment]["shell_sort"][str(2 ** power)][1])

powers = list(range(7, 16))
plt.plot(powers, insertionsort)
plt.plot(powers, selectionsort)
plt.plot(powers, mergesort)
plt.plot(powers, shellsort)
plt.yscale('log')
plt.legend(["insertion_sort", "selection_sort",
            "merge_sort", "shell_sort"])
plt.show()
