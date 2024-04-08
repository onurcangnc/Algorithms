import numpy as np
import time as t

# Bubble Sort
# Time Complexity: O(n^2)

start_time = t.time()
arr = np.array([56, 12, 78, 39, 23, 88, 45, 10, 91, 5])
size = len(arr)

def is_sorted(arr, size):
    for i in range(size-1):
        if arr[i] > arr[i+1]:
            return False
    return True

def bubbleSort(arr, size):
    for i in range(size-1):
        for j in range(size-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print("Original Array: ", arr)
if(is_sorted(arr, size)):
    print("Array is already sorted")
else:
    print("Sorted Array: ", bubbleSort(arr, size))
end_time = t.time()
print("Time taken: ", end_time-start_time, "seconds")