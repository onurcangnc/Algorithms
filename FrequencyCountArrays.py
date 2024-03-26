import numpy as np
import time

start_time = time.time()
A = np.array([[1,3,4],
     [5,6,2],
     [7,5,1]])

B = np.array([[5,3,4],
     [2,1,6],
     [6,7,8]])

C = np.array([[0,0,0],
     [0,0,0],
     [0,0,0]])

C = A + B

print(C)
end_time = time.time()
print("Time:", end_time)