import timeit
import random
import csv

def insertion_sort(arr):
    n = len(arr)

    if n <= 1:
        return

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                myList[k] = left[i]
                i += 1
            else:
                myList[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            myList[k] = right[j]
            j += 1
            k += 1

def test_sorting(sort_function, array_size, repetitions):
    arr = [random.randint(1, 1000) for _ in range(array_size)]

    def wrapper():
        arr_copy = arr.copy()
        sort_function(arr_copy)

    time_taken = timeit.timeit(wrapper, number=repetitions)

    return time_taken / repetitions


n_sizes = [i for i in range(1, 100)]
insert_times = []
merge_times = []

for n in n_sizes:
    insertion_sort_time = test_sorting(insertion_sort, n, 5000)
    merge_sort_time = test_sorting(merge_sort, n, 5000)

    insert_times.append(f"{insertion_sort_time*1000000:.6f}")
    merge_times.append(f"{merge_sort_time*1000000:.6f}")

rows = zip(n_sizes, insert_times, merge_times)
csv_output = 'output3.csv'
with open(csv_output, mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Input Size", "Insertion Sort Time", "Merge Sort Time"])
    csv_writer.writerows(rows)



