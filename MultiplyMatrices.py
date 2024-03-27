import time
from numpy import array
from numpy import dot
'''
Frequency Count Method
'''

start_time = time.time()
matrix1 = array([[73,14,56],
           [29,88,42],
           [5,67,91]])

matrix2 = array([[37,68,20],
           [83,11,52],
           [95,63,24]])

result = dot(matrix1, matrix2)

print(result)
end_time = time.time()
print("Time taken: ", end_time - start_time)
