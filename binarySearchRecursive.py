import time
from numpy import array

'''
    Binary Search Recursive
'''

start_time = time.time()

A = array([3,6,8,12,14,17,25,29,31,36,42,47,53,55,62])
low = 0
high = len(A) - 1

def BinarySearchRecursive(A,low,high,key):
    if low == high:
        if A[low] == key:
            return low
        else:
            return -1
    else:
        mid = (low + high) // 2
        if key == A[mid]:
            return mid
        elif key < A[mid]:
            return BinarySearchRecursive(A,low,mid-1,key)
        else:
            return BinarySearchRecursive(A,mid+1,high,key)
    
print("Enter the value to search: ")
key = int(input())
print("Search value index is: ", BinarySearchRecursive(A,low,high,key))