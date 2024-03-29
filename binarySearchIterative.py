from numpy import array
import time

'''
Binary Search Iterative
Time: 1.8492388725280762
'''

start_time = time.time() 
A = array([3,6,8,12,14,17,25,29,31,36,42,47,53,55,62])
size = len(A)

def binarySearch(A,size,key):
    low = 0
    high = size - 1
    while low <= high:
        mid = (low + high) // 2
        if key == A[mid]:
            return mid
        elif key < A[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

searchValue = int(input("Enter the value to search: "))
result = binarySearch(A,size,searchValue)
if result == -1:
    print("Value not found")
else:
    print("Search value index is ", result)
end_time = time.time()
print("Time taken to search is: ", end_time - start_time)