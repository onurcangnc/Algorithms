import numpy as np

arr = np.array([56, 12, 78, 39, 23, 88, 45, 10, 91, 5])
size = len(arr)

def bubbleSort(arr, size):
    for i in range(size-1):
        for j in range(size-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print("Original Array: ", arr)
print("Sorted Array: ", bubbleSort(arr, size))