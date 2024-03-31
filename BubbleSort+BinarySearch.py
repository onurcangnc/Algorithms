'''
    Binary Search Algorithm with Bubble Sort Algorithm
'''

A = [56, 12, 78, 39, 23, 88, 45, 10, 91, 5]
print("Original Array: ", A)
size = len(A)

def bubbleSort(A, size):
    for i in range(size-1):
        for j in range(size-i-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A

sortedA = bubbleSort(A, size)
print("Sorted Array: ", sortedA)

def binarySearch(sortedA, size, key):
    low = 0
    high = size-1
    while low <= high:
        mid = (low + high) // 2
        if key == sortedA[mid]:
            return mid
        elif key < sortedA[mid]:
            high = mid -1
        else:
            low = mid + 1
    return -1

searchValue = int(input("Enter the value to search: "))
if binarySearch(sortedA, size, searchValue) == -1:
    print("Value not found")
else:
    print("Search value index is ", binarySearch(sortedA, size, searchValue))