import random
import timeit

# Алгоритм сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Алгоритм сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

# Генерація наборів даних
array_sizes = [100, 1000, 5000]
data_types = ["Random", "Sorted", "Reverse Sorted"]

datasets = {}
for size in array_sizes:
    datasets[f'{size}_Random'] = [random.randint(0, size) for _ in range(size)]
    datasets[f'{size}_Sorted'] = sorted(datasets[f'{size}_Random'])
    datasets[f'{size}_Reverse'] = datasets[f'{size}_Sorted'][::-1]

# Вимірювання часу виконання
execution_times = {'Insertion Sort': {}, 'Merge Sort': {}, 'Timsort': {}}
number_of_runs = 3

for name, arr in datasets.items():
    for sort_algorithm in ('Insertion Sort', 'Merge Sort', 'Timsort'):
        if sort_algorithm == 'Insertion Sort':
            timer = timeit.Timer(lambda: insertion_sort(arr.copy()))
        elif sort_algorithm == 'Merge Sort':
            timer = timeit.Timer(lambda: merge_sort(arr.copy()))
        else:
            timer = timeit.Timer(lambda: sorted(arr.copy()))

        execution_times[sort_algorithm][name] = timer.timeit(number=number_of_runs) / number_of_runs

execution_times
